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

from libs.ardmediathek_client import ArdMediathekClient

if __name__ == '__main__':
    addon_id = 'plugin.video.inasnacht'
    mediathek_id = 'Y3JpZDovL2Rhc2Vyc3RlLm5kci5kZS8xNDA5'

    app = ArdMediathekClient(addon_id, mediathek_id)
    app.DoSome()

