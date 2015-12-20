#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @file
 @brief This file contains the QDvGrab Preferences dialog (i.e Preferences of QDvgrab)
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

import sys
import os
# Need for path
import os.path
#Need for find library
import shutil
#Need for create command line
import subprocess

#need for display gui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from preferencesui import Ui_Dialog
from kviso import KvIso



class PreFerences(QDialog):
    def __init__(self):
        super(PreFerences, self).__init__()
        self.setupUi()
        #self.createWidgets()
        self.connectActions()
        self.updateUi()

    #===========================================================================
    def setupUi(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    #===========================================================================
    def connectActions(self):
        #pass
        self.ui.btncredits.clicked.connect(self.Credits)
        self.ui.btndvgrab.clicked.connect(self.dvgrabpath)
        self.ui.btntranscode.clicked.connect(self.transcodepath)
        self.ui.btnchoosefile.clicked.connect(self.outputpath)
        self.ui.cmblanguages.activated.connect(self.languages)

    #===========================================================================
    def updateUi(self):
        self.ui.lbltranscode.setEnabled(False)
        self.ui.lnetranscode.setEnabled(False)
        self.ui.btntranscode.setEnabled(False)
        self.ui.chkactivepreview.isChecked(True)


    #===========================================================================
    def Credits(self):
        " run the Credits dialog "
        self.windo = KvIso()
        self.windo.exec_()

    #===========================================================================
    def dvgrabpath(self):
        pass

    #===========================================================================
    def transcodepath(self):
        pass

    #===========================================================================
    def outputpath(self):
        pass

    #===========================================================================
    def languages(self):
        pass

    #===========================================================================


if __name__ == "__main__":
    application = QApplication(sys.argv)
    PreFerences = PreFerences()
    PreFerences.show()
    application.exec_()