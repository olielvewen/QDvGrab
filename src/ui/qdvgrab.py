#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @file
 @brief This file contains the QDvGrab dialog (i.e A tool for grab videos from Dv Camecorders)
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
from qdvgrabui import Ui_MainWindow
from preferences import PreFerences
from credits import Credits
from about import About

#others settings file
import info

app_name = "QDvGrab"
app_version = "0.10"
app_author = "Olivier Girard"
author_mail = "olivier@openshot.org"

QualityList = {} #dico quality audio
FpsList = {} #dico fps
Variables = {"Cmd: " " #command to execute",
             "CmdList: [] #list commands to execute",
             "ConfigFolder: os.path.join(QDir.homePath(), .qdvgrab)",
             "ConfigFile: os.path.join(QDir.homePath(), .qdvgrab/logfile)",
             "FileNameOutput: "" #filename output os.path.basename()",
             "DeviceOutput: "" #Device name Camecorder",
             "DirectNameOutput: " " #name of output folder os.path.direname()",
             "TempFolderName: " " #name of temporary folder",
             "TempFolderOutput: "" #name of folder output"
             }
#check if we are on Linux either exit
if (os.name != "posix"):
    print("You are not under Linux system")
    sys.exit(2)

class QdvGrab(QMainWindow):
    def __init__(self, parent=None):
        super(QdvGrab, self).__init__(parent)
        self.setupUi()
        self.connectActions()
        self.updateUi()
        # self.centerScreen()

        # def centerScreen(self):
        ##geometry_window = ""
        ##self.geometry_window = geometry_window

        # if self.geometry_window:
        # self.resize(geometry_window[0], geometry_window[1])
        # else:
        # self.geometry_window = (self.geometry().width(), self.geometry().height())

        ##size_screen = QDesktopWidget().screenGeometry()
        ##self.move(((size_screen.width() - geometry_window.width())/2), ((size_screen.height() - geometry_window.height()))/2)

    # ==================================================================================================================
    def setupUi(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # ==================================================================================================================
    def connectActions(self):
        """ Function doing connection not done by Qt Designer """
        self.ui.btnacquisitiondv.clicked.connect(self.Recording)
        self.ui.btnrecordmpeg.clicked.connect(self.Recording)
        self.ui.btnstartrecord.clicked.connect(self.Acquisition)
        self.ui.btnpreferences.clicked.connect(self.run_preferences_screen)
        self.ui.btnhelp.clicked.connect(self.Help)
        self.ui.btnquit.clicked.connect(self.Quit)

        self.ui.actionOpen_Directory.triggered.connect(self.openDirectory)
        self.ui.actionQuit.triggered.connect(self.Quit)
        self.ui.actionPreferences.triggered.connect(self.run_preferences_screen)
        self.ui.actionAbout_Qt.triggered.connect(self.AboutQt)
        self.ui.actionAbout_QdvGrab.triggered.connect(self.AboutQdvgrab)

    # ==================================================================================================================
    def updateUi(self):
        self.ui.lnecapturename.setText("My Awesome Movie")
        self.ui.lnecapturename.setFocus()
        self.ui.lnecapturename.selectAll()

    # ==================================================================================================================
    def Recording(self):
        """ Run the type of acquisition asked """
        pass

    # ==================================================================================================================
    def Acquisition(self):
        """ Run the acquisition process i.e run dvgrab """
        pass

    # ==================================================================================================================
    def Help(self):
        """ Call the help webpage """
        self.windo = Credits()
        self.windo.exec_()

    # ==================================================================================================================
    def Quit(self):
        """ Close the application """
        application.quit()

    # ==================================================================================================================
    def run_preferences_screen(self):
        """ Run the Preferences Dialog """
        self.windo = PreFerences()
        self.windo.exec_()

    # ==================================================================================================================
    def closeEvent(self, event):
        """
        function run just before the mainwindow is closed and stop all work in progress and save settings
         """
        event.accept()

    #===================================================================================================================
    def openDirectory(self):
        pass

    #===================================================================================================================
    def AboutQt(self):
        """
        Method helping you to know which version of Qt you are using displaying an nice window
         """
        QMessageBox.aboutQt(QdvGrab)

    #===================================================================================================================
    def AboutQdvgrab(self):
        """
        Run the About Dialog
        :return:
        """
        self.windo = About()
        self.windo.show()

    #===================================================================================================================


if __name__ == "__main__":
    application = QApplication(sys.argv)
    QdvGrab = QdvGrab()
    QdvGrab.show()
    print("Welcome to QDvGrab {}. \nHope you'll enjoy it. \nPlease report all bugs,"
          "features request and comments at {}\n".format(app_version, author_mail))
    application.exec_()
