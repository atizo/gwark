# -*- coding: utf-8 -*-
#
# Atizo - The Open Innovation Platform
# http://www.atizo.com/
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

from django.core.management.base import BaseCommand, CommandError
from django.core import serializers

from django.conf import settings
from django.db.models.loading import get_app
import os

APP_PREFIX = 'gwark.'
DJANGO_APP_PREFIX = 'django.'

DUMP_FORMAT = 'json'
DUMP_INDENT = 4
DUMP_FIXTRUES_DIR = "fixtures/"
EXTERNAL_FIXTURES_DIR = os.path.join(settings.PROJECT_ROOT, 'external_fixtures')

EXCLUDE_MODEL = ['Permission', 'LogEntry', 'AsyncExecution']
EXCLUDE_APPS = ['django.contrib.sessions', 
                'django.contrib.contenttypes', 
                'rosetta',
                'atizo',
                'reversion',                
                'django.contrib.sites',
                'django_extensions'
                ]

class Command(BaseCommand):

    help = 'Output the contents of the atizo models as fixtures'

    def _dump_files(self, path, file, objects):
        json_file = os.path.join(path, file)
        # empty files are impossible to load
        if len(objects) > 0:
            try:
                os.makedirs(path)
            except OSError:
                pass
            
            print '%d to %s' % (len(objects), json_file) 
            f = open(json_file, 'w')
            try:
                f.write(serializers.serialize(DUMP_FORMAT, objects, indent=DUMP_INDENT, use_natural_keys=True))
            except Exception, e:
                raise CommandError("Unable to serialize database: %s" % e)                
            f.close()
        elif os.path.exists(json_file):
            print '-------> Remove empty file (impossible to load) %s' % json_file
            
    def _dump_atizo_apps(self, app_list):
        from django.db.models import get_models
        for app in app_list:
            if not app:
                continue
            model_list = get_models(app)            
            app_base_path = os.path.dirname(app.__file__)
            for model in model_list:
                if not model.__name__ in EXCLUDE_MODEL:
                    path = os.path.join(app_base_path, DUMP_FIXTRUES_DIR).replace('/models', '')
                    file = "%s.%s" % (model.__name__.lower(), DUMP_FORMAT)    
                    self._dump_files(path, file, model.objects.all())
                
    def _dump_extrenal_apps(self, app_list): 
        from django.db.models import get_models
        for app in app_list:
            if app[1] is not None:
                model_list = get_models(app[1])
                for model in model_list:
                    objects = set()
                    if not model.__name__ in EXCLUDE_MODEL:
                        objects.update(model.objects.all())
                        path = os.path.join(EXTERNAL_FIXTURES_DIR).replace('/models', '')
                        file = "%s_%s.%s" % (app[0].replace('.', '_'), model.__name__.lower(), DUMP_FORMAT)
                        self._dump_files(path, file, objects)

    def handle(self, *app_labels, **options):
        app_label = lambda app: app[app.rfind('.')+1:]
        
        atizo_app_list = []
        extrenal_app_list = []
        
        for app in settings.INSTALLED_APPS:
            if app not in EXCLUDE_APPS:
                if app.startswith(APP_PREFIX):
                    atizo_app_list.append(get_app(app_label(app), True))
                else:
                    extrenal_app_list.append((app, get_app(app_label(app), True)))
        try:
            serializers.get_serializer(DUMP_FORMAT)
        except KeyError:
            raise CommandError("Unknown serialization format: %s" % DUMP_FORMAT)
        
        print '\ndump atizo data:'
        self._dump_atizo_apps(atizo_app_list)
        print '\ndump external data:'
        self._dump_extrenal_apps(extrenal_app_list)