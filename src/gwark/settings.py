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

try:
    from settings_local import *
except ImportError:
    pass

TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS
TIME_ZONE = 'Europe/Zurich'
LANGUAGE_CODE = 'de'
ugettext = lambda s: s

LANGUAGES = (
    ('de', u'Deutsch'),
    ('en', u'English'),
    ('fr', u'Français'),
)

LANGUAGES_DICT = {}
for k,v in LANGUAGES:
    LANGUAGES_DICT[k] = v

SUPPORTED_LANGUAGES = set([
    'de',
    'en',
    'fr',
])

DATE_FORMAT = ugettext(u"%d.%m.%Y")
DATETIME_FORMAT = ugettext(u"%d.%m.%Y %H:%M")
TIME_FORMAT = ugettext(u"%H:%M")

SITE_ID = 1
USE_I18N = True
MEDIA_URL = '/site_media/'
ADMIN_MEDIA_PREFIX = '/media/'
ADMIN_URL = 'guru'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'grx!dkji&hxpb5oynzd$ud_%)t!ccl)7vh1k!k100x8_r*r)d^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'gwark.urls'

FIXTURE_DIRS = (
    'external_fixtures/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'gwark.apps.core'
)
