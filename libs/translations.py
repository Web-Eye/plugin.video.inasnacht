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

class translations:

    DURATION = 'duration'
    BROADCASTEDON = 'broadcastedon'
    AVAILABLETO = 'availableto'
    HOURS = 'hours'
    MINUTES = 'minutes'
    SECONDS = 'seconds'

    def __init__(self, addon):
        self._language = addon.getLocalizedString

    def getString(self, name):

        return {
            self.DURATION:          self._language(30100),
            self.BROADCASTEDON:     self._language(30101),
            self.AVAILABLETO:       self._language(30102),
            self.HOURS:             self._language(30103),
            self.MINUTES:           self._language(30104),
            self.SECONDS:           self._language(30105)
        }[name]
