#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @file
 @brief This file contains the QDvGrab Credits dialog (i.e Credits for QdvGrab Project)
 @author Olivier Girard <olivier@openshot.org>

 @section LICENSE

 Copyright (c) 2014-2015 QDvGrab Team. This file is part of
 QDvGrab (http://www.qdvgrab.org), an open-source project
 dedicated to delivering high quality video editing and animation solutions
 to the world.

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
# Need for find library
import shutil
# Need for create command line
import subprocess
#need for create temporary file in the temp folder
from tempfile import TemporaryDirectory

# need for display gui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# Used for call ui files
from creditsui import Ui_creditscreen

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
        PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        path_license = os.path.join(PATH, 'LICENSE')

        with open('path_license', 'r') as my_license:
            text = my_license.read()

            self.ui.textBrowserlicense.append(text)

    #===================================================================================================================

if __name__ == "__main__":
    application = QApplication(sys.argv)
    Credits = Credits()
    Credits.show()
    application.exec_()