# -*- coding: utf-8 -*-
# Copyright 2021 WebEye
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

import requests
import json


def _getContent(url):
    page = requests.get(url)
    return json.loads(page.content)


class ARDMediathekAPI:

    def __init__(self, url, tag):

        self._posterWidth = 480

        if tag is not None:
            pageNumber = tag.get('pageNumber')
            pageSize = tag.get('pageSize')
            url = url.replace('{pageNumber}', str(pageNumber))
            url = url.replace('{pageSize}', str(pageSize))
            self._posterWidth = tag.get('posterWidth')

        self._content = _getContent(url)

    def _hasContent(self):
        return self._content is not None

    def getPagination(self):
        if self._hasContent():
            return self._content['pagination']

    def getTeaser(self):
        try:
            teasers = []
            if self._hasContent():
                for teaser in self._content['teasers']:
                    image = teaser['images']['aspect16x9']['src'].replace('{width}', str(self._posterWidth))
                    teasers.append({'availableTo': teaser['availableTo'],
                                    'broadcastedOn': teaser['broadcastedOn'],
                                    'duration': teaser['duration'],
                                    'poster': image,
                                    'title': teaser['longTitle'],
                                    'url': teaser['links']['target']['href']})

                return teasers
        finally:
            pass

