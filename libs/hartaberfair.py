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
import json
import sys
import urllib
import urllib.parse
from datetime import datetime

from libs.ardmediathek_api import ARDMediathekAPI
from libs.kodion.gui_manager import GuiManager
from libs.kodion.utils import utils as kodionUtils
from libs.utils import utils

# -- Constants ----------------------------------------------
ADDON_ID = 'plugin.video.hartaberfair'
BASEURL = 'https://api.ardmediathek.de/page-gateway/widgets/daserste/asset/Y3JpZDovL3dkci5kZS9oYXJ0IGFiZXIgZmFpcg?pageNumber={pageNumber}&pageSize={pageSize}&embedded=true&seasoned=false&seasonNumber=&withAudiodescription=false&withOriginalWithSubtitle=false&withOriginalversion=false'
PAGESIZE = 30
POSTERWIDTH = 480

# ADDONTHUMB = utils.translatePath('special://home/addons/' + ADDON_ID + '/resources/assets/icon.png')
FANART = kodionUtils.translatePath('special://home/addons/' + ADDON_ID + '/resources/assets/fanart.jpg')
DEFAULT_IMAGE_URL = ''

guiManager = GuiManager(sys.argv[1], ADDON_ID, DEFAULT_IMAGE_URL, FANART)
guiManager.setContent('movies')

# -- Settings -----------------------------------------------
addon = kodionUtils.getAddon(ADDON_ID)


def setHomeView(url, tag=None):
    API = ARDMediathekAPI(url, tag)
    pagination = API.getPagination()
    teasers = API.getTeaser()

    if teasers is not None:
        for teaser in teasers:
            title = teaser['title']
            duration = utils.getDuration(int(teaser['duration']))
            broadcastedOn = utils.getDateTime(teaser['broadcastedOn'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d.%m.%Y, %H:%M:%S')
            availableTo = utils.getDateTime(teaser['availableTo'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d.%m.%Y, %H:%M:%S')
            plot = f'[B]{title}[/B]\n\n[B]Duration[/B]: {duration}\n[B]Broadcasted on[/B]: {broadcastedOn}\n[B]Available To[/B]: {availableTo}'

            guiManager.addDirectory(title, teaser['poster'], plot, buildArgs('list', teaser['url']))

        if pagination is not None:
            pageNumber = int(pagination['pageNumber'])
            pageSize = int(pagination['pageSize'])
            totalElements = int(pagination['totalElements'])

            if totalElements > ((pageNumber + 1) * pageSize):
                strPageNumber = str(pageNumber + 2)
                tag = {
                    'pageNumber': pageNumber + 1,
                    'pageSize': PAGESIZE,
                    'posterWidth': POSTERWIDTH
                }
                guiManager.addDirectory(f'Page {strPageNumber}', None, None, buildArgs('home', BASEURL, json.dumps(tag)))


def get_query_args(s_args):
    args = urllib.parse.parse_qs(urllib.parse.urlparse(s_args).query)
    print(args)

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
        tag = {
            'pageNumber': 0,
            'pageSize': PAGESIZE,
            'posterWidth': POSTERWIDTH
        }

        args = buildArgs('home', BASEURL, tag)

    method = args.get('method')
    url = args.get('url')
    tag = args.get('tag')

    if tag is not None and isinstance(tag, str):
        tag = json.loads(tag)

    {
        'home': setHomeView
    }[method](url, tag)

    guiManager.endOfDirectory()
