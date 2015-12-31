#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @file
 @brief This file contains the QDvGrab Preferences dialog (i.e Preferences of QDvgrab)
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
from credits import Credits

#Need others settings file
#import info



class PreFerences(QDialog):
    def __init__(self):
        super(PreFerences, self).__init__()
        self.setupUi()
        #self.createWidgets()
        self.connectActions()
        self.updateUi()

    #===================================================================================================================
    def setupUi(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    #===================================================================================================================
    def connectActions(self):
        """ connection of all events """
        self.ui.btncredits.clicked.connect(self.Credits)
        self.ui.btndvgrab.clicked.connect(self.dvgrabpath)
        self.ui.btntranscode.clicked.connect(self.transcodepath)
        self.ui.btnchoosefile.clicked.connect(self.outputpath)
        self.ui.cmblanguages.activated.connect(self.languages)
        self.ui.rdbdvraw.toggled.connect(self.choosedvformat)
        self.ui.rdbdv2.toggled.connect(self.choosedvformat)
        self.ui.rdbdv.toggled.connect(self.choosedvformat)
        self.ui.rdbhdv.toggled.connect(self.choosehdvformat)
        self.ui.rdbmpeg2.toggled.connect(self.choosehdvformat)
        self.ui.chknone.toggled.connect(self.chooseautomaticconversion)
        self.ui.chkdvraw.toggled.connect(self.chooseautomaticconversion)
        self.ui.chkdv2.toggled.connect(self.chooseautomaticconversion)
        self.ui.chkhdv.toggled.connect(self.chooseautomaticconversion)
        self.ui.chkdetection.toggled.connect(self.choosedetectionscene)
        self.ui.chkautomatic.toggled.connect(self.choosedetectionscene)
        self.ui.chkscene.toggled.connect(self.choosedetectionscene)
        self.ui.spbscene.valueChanged.connect(self.choosedetectionscene)
        self.ui.chkautomaticrecord.toggled.connect(self.captureextraparameters)
        self.ui.chkmanualrecord.toggled.connect(self.captureextraparameters)
        self.ui.lnehours.textChanged.connect(self.captureextraparameters)
        self.ui.lneminutes.textChanged.connect(self.captureextraparameters)
        self.ui.chkactivepreview.toggled.connect(self.runactivepreview)

    #===================================================================================================================
    def updateUi(self):
        self.ui.lbltranscode.setEnabled(False)
        self.ui.lnetranscode.setEnabled(False)
        self.ui.btntranscode.setEnabled(False)
        self.ui.chkactivepreview.setVisible(True)
        self.ui.chknone.setChecked(True)
        self.ui.rdbdvraw.setChecked(True)
        self.ui.rdbhdv.setChecked(True)
        self.ui.chkdetection.setChecked(True)
        self.ui.chkautomaticrecord.setChecked(True)

        #3 tab
        self.ui.chkmanualrecord.setEnabled(False)
        self.ui.lnehours.setEnabled(False)
        self.ui.lneminutes.setEnabled(False)
        self.ui.label_4.setEnabled(False)
        self.ui.label_5.setEnabled(False)
        self.ui.chkactivepreview.setEnabled(False)
        

    #===================================================================================================================
    def Credits(self):
        " run the Credits dialog "
        self.windo = Credits()
        self.windo.exec_()

    #===================================================================================================================
    def dvgrabpath(self):
        pass

    #===================================================================================================================
    def transcodepath(self):
        pass

    #===================================================================================================================
    def outputpath(self):
        pass

    #===================================================================================================================
    def languages(self):
        pass

    #===================================================================================================================
    def choosedvformat(self):
        pass

    #===================================================================================================================
    def choosehdvformat(self):
        pass

    #===================================================================================================================
    def chooseautomaticconversion(self):
        pass

    #===================================================================================================================
    def choosedetectionscene(self):
        pass

    #===================================================================================================================
    def runactivepreview(self):
        pass

    #===================================================================================================================
    def captureextraparameters(self):
        pass

    #===================================================================================================================


if __name__ == "__main__":
    application = QApplication(sys.argv)
    PreFerences = PreFerences()
    PreFerences.show()
    application.exec_()