#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# start_app.py - A Start file for running QDvgrab
# Copyright (c) 2020 Olivier Girard <olivier@openshot.org>
#
# QDvgrab is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# QDvgrab is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys

from PyQt5.QtWidgets import QApplication

from qdvgrab import QdvGrab

app_name = "QDvGrab"
app_version = "0.15"
app_author = "Olivier Girard"
author_mail = "olivier@openshot.org"

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = QdvGrab()
    window.show()
    print("Welcome to QDvGrab {}. \nHope you'll enjoy it. \nPlease report all bugs,"
          "features request and comments at {}\n".format(app_version, author_mail))

    rc = application.exec_()
    sys.exit(rc)
