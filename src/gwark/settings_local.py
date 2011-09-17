# -*- coding: utf-8 -*-
#
# Gwark
# http://www.gwark.com/
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

import logging.config
import os
import socket
import sys

DEBUG = True

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
LIB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../lib')
sys.path.insert(0, LIB_DIR)

logging.config.fileConfig(os.path.join(PROJECT_ROOT, 'environments/logging.conf'))

INTERNAL_IPS = ('127.0.0.1',socket.gethostbyname('platform.dev'))
SESSION_COOKIE_DOMAIN = 'aeby.dyndns.org'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media')
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

ADMINS = (
     ('You', 'you@example.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gwark',
        'USER': 'gwark_user',
        'PASSWORD': 'test',
        'HOST': '',
        'PORT': '',
    }
}

# memcached
CACHE_BACKEND = 'dummy:///'
CACHE_TIMEOUT_DEFAULT = 1800

FACEBOOK_APP_ID  = '176664465742395'
FACEBOOK_API_KEY = 'b61940d3357fea342d4e9d55a24bc214'
FACEBOOK_SECRET_KEY = '0f1a7dfa86ed51080efc29bf898bbed1'
FACEBOOK_REQUEST_PERMISSIONS = 'email'

TWITTER_CONSUMER_KEY = 'g600yxAMVMUQKBkqQNZg'
TWITTER_CONSUMER_SECRET_KEY = 'OoDnS8FKMnLQTTiVUNJ9OG5H2iZxRCf9aQ4fQVkvtU'
TWITTER_REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
TWITTER_AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authenticate'