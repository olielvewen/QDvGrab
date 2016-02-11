#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @file
 @brief credits.py - This file contains the QDvGrab Credits dialog (i.e Credits for QdvGrab Project)
 @author Olivier Girard <olivier@openshot.org>

 @section LICENSE

 Copyright (c) 2014-2016 QDvGrab Team. This file is part of
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

# Used to run it
import sys
import os

# Need for path
import os.path

# Need for display gui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Used for call ui files
from creditsui import Ui_creditscreen
import info

class Credits(QDialog):

    """
    This screen shows who has developed,documented, translated and the licence of the project

    """
    def __init__(self, parent=None):
        super(Credits, self).__init__(parent)
        self.setupUi()

    #===================================================================================================================
    def setupUi(self):

        self.ui = Ui_creditscreen()
        self.ui.setupUi(self)

    #===================================================================================================================
    def showCredits(self):

        #PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        #path_license = os.path.join(info.PATH, 'LICENSE')

        with open("(os.path.join(info.PATH, 'LICENSE'))", 'r') as my_license:
            text = my_license.read()

            self.ui.textBrowserlicense.append(text)

        #init authors
            authors = []
            for person in info.CREDITS['code']:
                name = person['name']
                email = person['email']
                authors.append("{} <{}>".format(name, email))
            self.ui.textBrowserwritten.append(str(authors))

        #init documenters
            authors = []
            for person in info.CREDITS['documentation']:
                name = person['name']
                email = person['email']
                authors.append("{} <{}>".format(name, email))
            self.ui.textBrowserdocumented.append(str(authors))

        #init translator
            authors = []
            for person in info.CREDITS['translation']:
                name = person['name']
                email = person['email']
                authors.append("{} <{}>".format(name, email))
            self.ui.textBrowsertranslated.append(str(authors))

    #===================================================================================================================

if __name__ == "__main__":
    application = QApplication(sys.argv)
    Credits = Credits()
    Credits.show()
    sys.exit(application.exec_())