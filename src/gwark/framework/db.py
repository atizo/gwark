# -*- coding: utf-8 -*-
#
# Gwark
# http://www.gwark.net/
#
# Copyright (c) 2008-2010 Atizo AG. All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#
import os
from subprocess import call

TMP_DUMP_DB = '/tmp/dump_gwark.out'

def reset_schema(database_config):
    from django.db import connection
    from django.db import transaction
    from django.conf import settings
    
    db_engine = database_config['ENGINE'].split('.')[-1]
    
    if db_engine in ['postgresql_psycopg2', 'postgresql']:
        sql_list = (
            'DROP  SCHEMA public CASCADE',
            'CREATE SCHEMA public AUTHORIZATION %s' % database_config['USER'],
            'GRANT ALL ON SCHEMA public TO postgres',
            'GRANT ALL ON SCHEMA public TO public',
            "COMMENT ON SCHEMA public IS 'standard public schema';",
        )

    elif db_engine == 'mysql':
        sql_list = (
            'DROP DATABASE %s' % database_config['DATABASE_NAME'],
            'CREATE DATABASE %s' % database_config['DATABASE_NAME'],
            'USE %s' % database_config['DATABASE_NAME']
        )
    elif db_engine == 'sqlite3':
        db_path = os.path.join(settings.PROJECT_ROOT, database_config['DATABASE_NAME'])
        if os.path.exists(db_path):
            print "Remove sqlite3 db file: %s" % db_path
            os.remove(db_path)
    else:
        raise NotImplementedError, "This database backend is not yet supported: %s" % db_engine
    
    cursor = connection.cursor()
    if sql_list and len(sql_list):
        for sql in sql_list:
            cursor.execute(sql)
    transaction.commit_unless_managed()
    
def dump_tmp_db(database_config):
    os.environ['PGPASSWORD'] = database_config['PASSWORD']
    database_config['tmp_dump'] = TMP_DUMP_DB
    call('pg_dump -U %(USER)s -F c -b -f %(tmp_dump)s %(NAME)s' % database_config, shell=True)
    
def restore_tmp_db(database_config):
    database_config['tmp_dump'] = TMP_DUMP_DB
    call('pg_restore -U %(USER)s -d %(NAME)s %(tmp_dump)s > /dev/null 2>&1' % database_config, shell=True)