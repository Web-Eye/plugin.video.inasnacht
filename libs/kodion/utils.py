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
    # import xbmcplugin
    # import xbmcgui
    import xbmcaddon
    import xbmcvfs
except ImportError:
    # import libs.emu.xbmc as xbmc
    # import libs.emu.xbmcplugin as xbmcplugin
    # import libs.emu.xbmcgui as xbmcgui
    import libs.emu.xbmcaddon as xbmcaddon
    import libs.emu.xbmcvfs as xbmcvfs


class Utils:

    @staticmethod
    def getAddon(_id):
        return xbmcaddon.Addon(id=_id)

    @staticmethod
    def translatePath(value):
        return xbmcvfs.translatePath(value)

    @staticmethod
    def getSetting(addon, name):
        return addon.getSetting(name)
