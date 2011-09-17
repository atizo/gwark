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

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = []

if settings.DEBUG:
    # Using this method is inefficient and insecure. Do not use this in a production setting. Use this only for development.
    urlpatterns += patterns('', (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}), )


urlpatterns += patterns('gwark.apps',
    url(r'^$', 'core.views.welcome', name='welcome'),
    url(r'^social/', include('socialregistration.urls')),
    #url(r'^accounts/', include('registration.backends.default.urls')),


    (r'^guru/doc/', include('django.contrib.admindocs.urls')),
    (r'^guru/', include(admin.site.urls)),
)
