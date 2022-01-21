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

try:
    # import xbmc
    import xbmcplugin
    import xbmcgui
    # import xbmcaddon
    # import xbmcvfs
except ImportError:
    # import libs.emu.xbmc as xbmc
    import libs.emu.xbmcplugin as xbmcplugin
    import libs.emu.xbmcgui as xbmcgui
    # import libs.emu.xbmcaddon as xbmcaddon
    # import libs.emu.xbmcvfs as xbmcvfs

import urllib.parse


class GuiManager:

    def __init__(self, argv, addon_id, default_image_url, fanart):
        self._argv = int(argv)
        self._addon_id = addon_id
        self._default_image_url = default_image_url
        self._fanart = fanart

        xbmcplugin.setPluginFanart(self._argv, self._fanart)

    def setContent(self, content):
        xbmcplugin.setContent(self._argv, content)

    def __setEntity(self, title, art, _property, _type, infolabels, isFolder, args):
        url = 'plugin://' + self._addon_id + '/?' + urllib.parse.urlencode(args)
        li = xbmcgui.ListItem(str(title))
        if art is not None:
            for item in art:
                li.setArt(item)

        if _property is not None:
            for item in _property:
                li.setProperty(str(item[0]), str(item[1]))

        if _type is not None and infolabels is not None:
            li.setInfo(type=_type, infoLabels=infolabels)

        xbmcplugin.addDirectoryItem(handle=self._argv, url=url, listitem=li, isFolder=isFolder)

    def addDirectory(self, title, poster=None, fanArt=None, _type=None, infoLabels=None, args=None):
        art = []
        _property = []

        if poster is not None:
            art.append({'thumb': poster})
        else:
            art.append({'thumb': self._default_image_url})

        if fanArt is not None:
            _property.append(['Fanart_Image', fanArt])
        elif self._fanart is not None:
            _property.append(['Fanart_Image', self._fanart])

        self.__setEntity(title, art, _property, _type, infoLabels, True, args)

        # url = 'plugin://' + self._addon_id + '/?' + urllib.parse.urlencode(args)
        # try:
        #     li = xbmcgui.ListItem(str(title))
        #     if poster is not None:
        #         li.setArt({'thumb': poster})
        #     else:
        #         li.setArt({'thumb': self._default_image_url})
        #     li.setProperty('Fanart_Image',  self._fanart)
        #
        #     if plot is not None:
        #         li.setInfo(type="Video", infoLabels={"Plot": str(plot)})
        #
        #     xbmcplugin.addDirectoryItem(handle=self._argv, url=url, listitem=li, isFolder=True)
        # except NameError:
        #     pass

    def endOfDirectory(self):
        xbmcplugin.endOfDirectory(self._argv)
