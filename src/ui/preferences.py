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
import info



class PreFerences(QDialog):
    def __init__(self, parent=None):
        super(PreFerences, self).__init__()

        self.parent = parent

        self.setupUi()
        self.connectActions()
        self.updateUi()

        QTimer.singleShot(0, self.loadsettings)
        #QTimer.singleShot(1000, self.dvgrabpath)

        format_capture = ['Dv Raw (.dv)', 'DV 2 (.avi)', 'Dv (.avi)', 'Dv Raw (.dv)', 'Mpeg 2 (.mpg)']
        for format in format_capture:
            self.ui.cmbformatcapture.addItem(format)
            self.ui.cmbformatcapture.setCurrentIndex(0)

        #populate the dvgrab path
        dvgrab_path = shutil.which('dvgrab')
        if dvgrab_path is not None:
            self.ui.lnedvgrab.setText(dvgrab_path)
        else:
            QMessageBox.information(self, self.tr("QDvGrab"), self.tr("Dvgrab is not installed"))

        transcode_path = shutil.which('transcode')
        self.ui.lnetranscode.setText(transcode_path)

    #===================================================================================================================
    def setupUi(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    #===================================================================================================================
    def connectActions(self):
        """
        connection of all events
        """
        self.ui.btncredits.clicked.connect(self.Credits)
        self.ui.btndvgrab.clicked.connect(self.dvgrabpath)
        self.ui.btntranscode.clicked.connect(self.transcodepath)
        self.ui.btnchoosefile.clicked.connect(self.outputpath)
        self.ui.cmblanguages.activated.connect(self.languages)
        self.ui.cmbformatcapture.activated.connect(self.chooseformatcapture)
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
        self.ui.chkdetection.setChecked(True)
        self.ui.chkautomaticrecord.setChecked(True)
        self.ui.lneoutputfile.setText("My Awesome Movie")
        self.ui.lneoutputfile.setFocus()
        self.ui.lneoutputfile.selectAll()

        #3 tab
        self.ui.chkmanualrecord.setEnabled(False)
        self.ui.lnehours.setEnabled(False)
        self.ui.lneminutes.setEnabled(False)
        self.ui.label_4.setEnabled(False)
        self.ui.label_5.setEnabled(False)
        self.ui.chkactivepreview.setEnabled(False)

        #2 tab
        self.ui.chkautomatic.setEnabled(False)
        self.ui.chkscene.setEnabled(False)
        self.ui.spbscene.setEnabled(False)
        self.ui.label_3.setEnabled(False)

        self.ui.chkdvraw.setEnabled(False)
        self.ui.chkdv2.setEnabled(False)
        self.ui.chkhdv.setEnabled(False)

    #===================================================================================================================
    def Credits(self):
        """
        run the Credits dialog
        :return:
        """
        self.windo = Credits()
        self.windo.exec_()

    #===================================================================================================================
    def dvgrabpath(self, result=""):
        """
        Display the path of dvgrab
        :return:
        """
        direct_repository = "/usr/bin"
        base_repository = QDir(direct_repository).absolutePath()

        dvgrab_path = QFileDialog.getOpenFileName(self, self.tr('QdvGrab - Choose a different path '), (QDir.rootPath() + base_repository))

        if dvgrab_path is not None:
            dvgrab_path =""
            result = QDir.absolutePath(dvgrab_path)
            #result = self.ui.lnedvgrab.text(base_repository)
            self.ui.lnedvgrab.append(result)

    #===================================================================================================================
    def transcodepath(self):
        """
        Display the path of transcode
        :return:
        """
        pass

    #===================================================================================================================
    def outputpath(self):
        """
        Display the output path by default and after this one choose by the user
        :return:
        """
        filePath = QFileDialog.getExistingDirectory(self, self.tr("QDvGab - Open a Directory"), QDir.homePath())

        if filePath:
            self.ui.lneoutputfile.setText(filePath)
    #===================================================================================================================
    def languages(self):
        """
        Display the language by default and if not or if the user would like to change it do it here
        :return:
        """
        pass

    #===================================================================================================================
    def chooseformatcapture(self):
        """
        Choose the capture format i.e either dv format or hdv format. And the main interface change thanks to this choice
        :return:
        """
        pass

    #===================================================================================================================
    def loadsettings(self):
        """
        :return: Here we load user settings and if none a basic config by default is loaded
        """
        settings = QSettings()

        filePath = settings.value('filePath')


        if filePath:
            self.ui.btnchoosefile.setText(filePath)

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