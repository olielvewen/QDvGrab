#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# preferences.py - A Preference screen for QDvgrab
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

import sys
import os
import os.path
import shutil

# need for display gui
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import QDir, QSettings, QLocale, QTimer

from ui.preferencesui import Ui_Dialog
from credits import Credits


class PreFerences(QDialog):
    def __init__(self, parent=None):
        super(PreFerences, self).__init__()

        self.parent = parent

        self.setupUi()
        self.connectActions()
        self.updateUi()

        QTimer.singleShot(0, self.loadSettings)

        format_capture = ['Dv Raw (.dv)', 'DV 2 (.avi)', 'Dv (.avi)', 'Hdv (.m2t)', 'Mpeg 2 (.mpg)', 'Mov (.mov)']
        for format in format_capture:
            self.ui.cmbformatcapture.addItem(format)
            self.ui.cmbformatcapture.setCurrentIndex(0)

        # populate the dvgrab path
        dvgrab_path = shutil.which('dvgrab')
        if dvgrab_path is not None:
            self.ui.lnedvgrab.setText(dvgrab_path)
        else:
            QMessageBox.information(self, self.tr("QDvGrab"), self.tr("Dvgrab is not installed"))

    # ==================================================================================================================
    def setupUi(self):

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Set Tooltips for preferences
        self.ui.cmblanguages.setToolTip(self.tr(" Change languages here "))
        self.ui.btnchoosefile.setToolTip(self.tr(" Choose here another directory other than this one by default "))
        self.ui.btndvgrab.setToolTip(self.tr(" Choose here another path other than this one by default if this one has failed "))
        self.ui.btncredits.setToolTip(self.tr(" Set the Credits Screen "))
        self.ui.cmbformatcapture.setToolTip(self.tr(" Select another format than this one by default"))
        self.ui.chknone.setToolTip(self.tr(" Select no conversion when acquisition is done "))
        self.ui.chkdvraw.setToolTip(self.tr(" Select Raw conversion when acquisition is done "))
        self.ui.chkdv2.setToolTip(self.tr(" Select Dv2 conversion when acquisition is done "))
        self.ui.chkhdv.setToolTip(self.tr(" Select Dv conversion when acquisition is done "))
        self.ui.chkdetection.setToolTip(self.tr(" Select only file when acquisition is done "))
        self.ui.chkautomatic.setToolTip(self.tr(" Set several files following hour and date when acquisition is done "))
        self.ui.chkscene.setToolTip(self.tr(" Creation of a scene when acquisition is done "))
        self.ui.chkautomaticrecord.setToolTip(self.tr("  Stop acquisition if not enought free space disk "))
        self.ui.chkmanualrecord.setToolTip(self.tr(" Planning the time of acquisition "))

    # ==================================================================================================================
    def connectActions(self):

        """
        connection of all events
        """
        self.ui.btncredits.clicked.connect(self.creDits)
        self.ui.btndvgrab.clicked.connect(self.dvgrabPath)
        self.ui.btnchoosefile.clicked.connect(self.outputPath)
        self.ui.cmblanguages.currentIndexChanged.connect(self.languageSelected)
        self.ui.cmbformatcapture.currentIndexChanged.connect(self.chooseFormatCapture)
        self.ui.chknone.toggled.connect(self.chooseAutomaticConversion)
        self.ui.chkdvraw.toggled.connect(self.chooseAutomaticConversion)
        self.ui.chkdv2.toggled.connect(self.chooseAutomaticConversion)
        self.ui.chkhdv.toggled.connect(self.chooseAutomaticConversion)
        self.ui.chkdetection.toggled.connect(self.chooseDetectionScene)
        self.ui.chkautomatic.toggled.connect(self.chooseDetectionScene)
        self.ui.chkscene.toggled.connect(self.chooseDetectionScene)
        self.ui.spbscene.valueChanged.connect(self.chooseDetectionScene)
        self.ui.chkautomaticrecord.toggled.connect(self.captureExtraParameters)
        self.ui.chkmanualrecord.toggled.connect(self.captureExtraParameters)
        self.ui.lnehours.textChanged.connect(self.captureExtraParameters)
        self.ui.lneminutes.textChanged.connect(self.captureExtraParameters)

    # ==================================================================================================================
    def updateUi(self):

        """
        Update the ui and desactive all widgets that we don't need for the moment

        """

        self.ui.chknone.setChecked(True)
        self.ui.chkdetection.setChecked(True)
        self.ui.chkautomaticrecord.setChecked(True)
        self.ui.lneoutputfile.setText("My Awesome Movie")
        self.ui.lneoutputfile.setFocus()
        self.ui.lneoutputfile.selectAll()

        # 3 tab
        self.ui.chkmanualrecord.setEnabled(False)
        self.ui.lnehours.setEnabled(False)
        self.ui.lneminutes.setEnabled(False)
        self.ui.label_4.setEnabled(False)
        self.ui.label_5.setEnabled(False)

        # 2 tab
        self.ui.chkautomatic.setEnabled(False)
        self.ui.chkscene.setEnabled(False)
        self.ui.spbscene.setEnabled(False)
        self.ui.label_3.setEnabled(False)

        self.ui.chkdvraw.setEnabled(False)
        self.ui.chkdv2.setEnabled(False)
        self.ui.chkhdv.setEnabled(False)

    # ==================================================================================================================
    def creDits(self):

        """
        run the Credits dialog

        """
        dialog = Credits()
        if dialog.exec_():
            dialog.show()

    # ==================================================================================================================
    def dvgrabPath(self):

        """
        Display the new path of dvgrab if he is not displayed by default

        """

        # select this folder by default when the QFileDialog is opened
        direct_repository = "/usr/bin"
        base_repository = QDir(direct_repository).absolutePath()

        new_dvgrab_path = QFileDialog.getOpenFileName(self, self.tr('QdvGrab - Choose a different path '), (QDir.rootPath() + base_repository))

        if new_dvgrab_path is not None:
            new_dvgrab_path = ""
            # clear the lineedit
            self.ui.lnedvgrab.clear()
            result = QDir(new_dvgrab_path).absolutePath()
            # result = self.ui.lnedvgrab.text(base_repository)
            self.ui.lnedvgrab.setText(result)

    # ==================================================================================================================
    def outputPath(self):

        """
        Display the output path by default and after this one choose by the user

        """
        new_output_path = QFileDialog.getExistingDirectory(self, self.tr("QDvGab - Open a Directory"), os.path.join(QDir.homePath() + "/Videos/"))
        new_output_path = str(self.ui.lneoutputfile.text())

        if new_output_path:
            self.ui.lneoutputfile.setText(new_output_path)

    # ==================================================================================================================
    def languageSelected(self, value):
        """
        Display the language by default and if not or if the user would like to change it do it here without changing
        this one of his desktop

        """
        pass

    # ==================================================================================================================
    def chooseFormatCapture(self):

        """
        Choose the capture format i.e either dv format or hdv format. And the main interface change thanks to this choice

        """
        
        pass

    # ==================================================================================================================
    def loadSettings(self):

        """
        Here we load user settings and if none a basic config by default is loaded

        """

        settings = QSettings()

        language = settings.value('language', type=str)

        new_output_path = settings.value('new_output_path', type=str)
        name_camcorder = settings.value('name_camcorder', type=str)

        formats_choose = settings.value('formats_choose', True, type=str)
        automatic_conversion = settings.value('automatic_conversion', True, type=bool)
        detection_scene = settings.value('detection_scene', True, type=bool)

        automatic_record = settings.value('automatic_record', True, type=bool)

        if language:
            value = self.ui.cmblanguages.addItem(language)
            self.ui.cmblanguages.setCurrentText(value)
        else:
            self.ui.cmblanguages.setCurrentText(language)
        if new_output_path:
            self.ui.lneoutputfile.setText(new_output_path)
        if name_camcorder:
            self.ui.lnenamecamcorder.setText(name_camcorder)
        if formats_choose:
            format = self.ui.cmbformatcapture.addItem(formats_choose)
            self.ui.cmbformatcapture.setCurrentText(format)
        else:
            self.ui.cmbformatcapture.setCurrentText(formats_choose)
        if automatic_conversion:
            self.ui.chknone.setChecked(True)
        if detection_scene:
            self.ui.chkdetection.setChecked(True)
        if automatic_record:
            self.ui.chkautomaticrecord.setChecked(True)

    # ==================================================================================================================
    def saveSettings(self):

        """
        Here we save users setting when the application is closed and if none a basic config by default is loaded

        """

        # MainWindowSettings
        language = QLocale.system().name()

        # GeneralSettings
        new_output_path = os.path.join(QDir.homePath() + "/Videos/")
        name_camcorder = self.ui.lnenamecamecorder.text()
        formats_choose = self.ui.cmbformatcapture.setCurrentIndex()

        # ConversionSettings
        automatic_conversion = self.ui.chknone.isChecked()
        detection_scene = self.ui.chkdetection.isChecked()

        # CaptureSettings
        automatic_record = self.ui.chkautomaticrecord.isChecked()

        settings = QSettings(QSettings.SystemScope, 'eCreate', 'qdvgrab')

        #settings.beginGroup('MainWindowSettings')
        #settings.setValue()
        #settings.setValue()
        #settings.endGroup()

        settings.beginGroup('GeneralSettings')
        settings.setValue('language', language)
        settings.setValue('new_output_path', new_output_path)
        settings.setValue('name_camcorder', name_camcorder)
        settings.endGroup()

        settings.beginGroup('ConversionSettings')
        settings.setValue('formats_choose', formats_choose)
        settings.setValue('automatic_conversion', automatic_conversion)
        settings.setValue('detection_scene', detection_scene)
        settings.endGroup()

        settings.beginGroup('CaptureSettings')
        settings.setValue('automatic_record', automatic_record)
        settings.endGroup()

    # ==================================================================================================================
    def chooseAutomaticConversion(self):

        """
        Several choices if the user would like to get directly his file in mpeg2 (not passing by a conversion tool after
        grabbing his film

        """
        pass

    # ==================================================================================================================
    def chooseDetectionScene(self):

        """
        The user can choose if he would like one file or severals

        """
        pass

    # ==================================================================================================================
    def captureExtraParameters(self):

        """
        The user can choose several parameters that he can't do anywhere like:
        - stop the grab if not enought space disks
        - program a time for the grab i.e for 50 minutes

        """
        pass
    # ==================================================================================================================
