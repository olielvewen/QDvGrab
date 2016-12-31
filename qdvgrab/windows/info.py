#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @file
 @brief This file contains a global settings file for the QDvGrab project
 @author Olivier Girard <olivier@openshot.org>

 @section LICENSE

 Copyright (c) 2014-2015 QDvGrab Team. This file is part of
 QDvGrab (http://www.qdvgrab.org), an open-source project
 dedicated to delivering a tiny and easy tool for dvgrab.

 QDvGrab is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 QDvGrab is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with QDVgrab.  If not, see <http://www.gnu.org/licenses/>.
 """

import os

app_name = "QDvGrab"
app_version = "0.10"
app_author = "Olivier Girard"
author_mail = "olivier@openshot.org"
app_date_version = "2015122900000"
gpl_version = '3'
SUPPORTED_LANGUAGES = ['English', 'French']
PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
HOME_PATH = os.path.join(os.path.expanduser("~"))
USER_PATH = os.path.join(HOME_PATH, ".qdvgrab")
TEMP_PATH = os.path.join(USER_PATH, "Temp")

#name of all contributors to the project
OG = {'name': u'Olivier Girard', 'email': 'olivier@openshot.org'}

#credits
CREDITS = {
    'code'         : [OG],
    'documentation': [OG],
    'translation'  : [OG],
}

SETUP = {
    'name' : app_name,
    'version' : app_version,
    'date'    : app_date_version,
    'license' : 'GNU GPL v.' + gpl_version,
    'author'  : app_author,
    'email'   : author_mail,
    'url'     : 'https://github.com/olielvewen/QDvGrab/',
    'description' : "Grab film on the hard drive in a easy way from a DV or HDV camecorder",
}