#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @file
 @brief This file contains the QDvGrab About dialog (i.e About for QdvGrab Project)
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
import platform

# Need for find library

# need for display gui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Used for call ui files
from aboutui import Ui_aboutscreen
from credits import Credits

#Need others settings files
import info


app_name = "QDvGrab"
app_version = "0.10"
app_author = "Olivier Girard"
author_mail = "olivier@openshot.org"

class About(QDialog):

    """
    This screen shows the resume of the project

    """
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi()
        self.connectActions()

        self.parent = parent

    #===================================================================================================================
    def setupUi(self):

        self.ui = Ui_aboutscreen()
        self.ui.setupUi(self)

        self.ui.lblimageicon.setPixmap(QPixmap("tool-animator.png"))
        self.ui.lblimageicon.setMaximumSize(QSize(220, 340))
        self.ui.lblimageicon.setScaledContents(True)

        project_name = ("<b>{} - {}</b>".format(app_name, app_version))
        self.ui.lblprojectname.setText(project_name)

        version_program = ("<b>Python {} - Qt {} - PyQt {}</b>".format(platform.python_version(), QT_VERSION_STR, PYQT_VERSION_STR))
        self.ui.lblversionplateform.setText(version_program)

    #===================================================================================================================
    def connectActions(self):

        """


        """
        self.ui.btncredits.clicked.connect(self.runCredits)

    #===================================================================================================================
    def runCredits(self):

        """
        Run the Credits Dialog

        """
        self.windo = Credits()
        self.windo.exec_()

    #===================================================================================================================

if __name__ == "__main__":
    application = QApplication(sys.argv)
    About = About()
    About.show()
    application.exec_()
