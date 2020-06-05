#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# about.py - A About screen for QDvgrab
# Copyright (c) 2014-2016-2019-2020 Olivier Girard <olivier@openshot.org>
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

# Used to run it
import sys
import os

# Need for path
import platform

# Need for display gui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, QT_VERSION_STR, PYQT_VERSION_STR, pyqtSlot
from PyQt5.QtWidgets import QDialog

# Used for call ui files
from ui.aboutui import Ui_aboutscreen
from credits import Credits

app_name = "QDvGrab"
app_version = "0.13"
app_author = "Olivier Girard"
author_mail = "olivier@openshot.org"


class About(QDialog):

    """
    This screen shows the resume of the project
    """

    def __init__(self, *args, **kwargs):
        super(About, self).__init__(*args, **kwargs)
        self.setupUi()

    # ==================================================================================================================
    def setupUi(self):

        self.ui = Ui_aboutscreen()
        self.ui.setupUi(self)

        icon_path = os.path.join(os.path.dirname(__file__), "./images/tool-animator.png")
        self.ui.lblimageicon.setPixmap(QPixmap(icon_path))
        self.ui.lblimageicon.setMaximumSize(QSize(220, 340))
        self.ui.lblimageicon.setScaledContents(True)

        project_name = ("<b>{} - {}</b>".format(app_name, app_version))
        self.ui.lblprojectname.setText(project_name)

        version_program = ("<b>Python {} - Qt {} - PyQt {}</b>".format(platform.python_version(), QT_VERSION_STR, PYQT_VERSION_STR))
        self.ui.lblversionplateform.setText(version_program)

    # ==================================================================================================================
    @pyqtSlot()
    def runCredits(self):

        """
        Run the Credits Dialog

        """

        self.windo = Credits()
        self.windo.exec_()

    # ===================================================================================================================


