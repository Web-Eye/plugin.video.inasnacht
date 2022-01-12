# -*- coding: utf-8 -*-
# Copyright 2022 WebEye
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import urllib
import urllib.parse

try:
    import xbmc
    import xbmcplugin
    import xbmcgui
    import xbmcaddon
    import xbmcvfs
except ImportError:
    import libs.emu.xbmc as xbmc
    import libs.emu.xbmcplugin as xbmcplugin
    import libs.emu.xbmcgui as xbmcgui
    import libs.emu.xbmcaddon as xbmcaddon
    import libs.emu.xbmcvfs as xbmcvfs

# -- Constants ----------------------------------------------
ADDON_ID = 'plugin.video.hartaberfair'


# -- Settings -----------------------------------------------
addon = xbmcaddon.Addon(id=ADDON_ID)
xbmcplugin.setContent(int(sys.argv[1]), 'movies')


def setHomeView(url, tag=None):
    pass


def get_query_args(s_args):
    args = urllib.parse.parse_qs(urllib.parse.urlparse(s_args).query)

    for key in args:
        args[key] = args[key][0]
    return args


def buildArgs(method, url=None, tag=None):
    return {
        'method': method,
        'url': url,
        'tag': tag
    }


def hartaberfair():

    args = get_query_args(sys.argv[2])
    if args is None or args.__len__() == 0:
        args = buildArgs('home')

    method = args.get('method')
    url = args.get('url')
    tag = args.get('tag')

    {
        'home': setHomeView
    }[method](url, tag)

    xbmcplugin.endOfDirectory(int(sys.argv[1]))
