#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @file
 @brief This file contains the Q dialog (i.e A tool for )
 @author Olivier Girard <olivier@openshot.org>

 @section LICENSE

 Copyright (c) 2015 Q Team. This file is part of
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

#Used for system
import sys
#Used for functions
import os
#Need for path
import os.path
#Need for find library
import shutil
#Need for create command line
import subprocess
#Used to run the web browser by default
import webbrowser
#need for display gui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#Used for call ui files
from kvisoui import Ui_kvisodialog

class KvIso(QDialog):

    def __init__(self):
        super(KvIso, self).__init__()
        self.createWidgets()
        self.setupUi()
        self.connectActions()

        #self.UpdateProgressBar(0)
    #===================================================================================================================
    def createWidgets(self):
        self.ui = Ui_kvisodialog()
        self.ui.setupUi(self)

    #===================================================================================================================
    def connectActions(self):
        self.ui.btnquit.clicked.connect(self.close)
        self.ui.btnhelp.clicked.connect(self.help)
        self.ui.btnchoosevideofile.clicked.connect(self.choosevideofile)
        self.ui.chkvideofile.toggled.connect(self.ui.chkimageiso.setEnabled)
        self.ui.chkimageiso.toggled.connect(self.ui.lnenamedvd.setEnabled)
        self.ui.btnexport.clicked.connect(self.export)
        self.ui.btncancel.clicked.connect(self.cancel)

    #===================================================================================================================
    def setupUi(self):
        self.ui.chkvideofile.setEnabled(False)
        self.ui.chkimageiso.setEnabled(False)
        self.ui.lnenamedvd.setEnabled(False)
        self.ui.btncancel.setEnabled(False)

    #===================================================================================================================
    def help(self, event):
        try:
            webbrowser.open("https://launchpad.net/DvdCreator")
            self.ui.textEdit.append("Website Project is open")
        except:
            QMessageBox.information(self, self.tr("Error!"), self.tr("Unable to open the website"))
            self.ui.textEdit.append("Unable to open the website")

    #===================================================================================================================
    def choosevideofile(self):
        self.filepath = ""
        #self.file_extension = ("MPG Files (*.MPG), MPEG Files (*.mpeg), MPG Files (*.dvd)")
        self.filedialog = QFileDialog()
        self.filepath = self.filedialog.getOpenFileNames(self, self.tr('Kviso'), self.tr('Choose a MPEG file'))
        if self.filepath:
            #self.btnchoosevideofile.setText(str(filepath))
            self.ui.textEdit.setReadOnly(True)
            #efface toute trace d'une precedante utilisation si pas faite
            self.ui.textEdit.clear()
            #Efface l'exportation precedante si pas faite
            self.ui.progressbarexport.reset()

            self.p1 = str(self.filepath).split('/')
            self.p1.pop()
            self.path = '/'.join(self.p1) + '/'

            self.ui.chkvideofile.setEnabled(True)
            #self.ui.textEdit.toPlaintText()

    #===================================================================================================================
    def export(self):
        if self.ui.chkvideofile.isChecked():
            self.processus = QProcess()
            #command = ["dvdauthor -o (self.path + 'dvd') str(self.filepath)"]
            command = ["tcmodinfo -p"]
            self.processus.setArguments(command)
            #self.processus.setArguments("dvdauthor")
            #self.processus.setArguments("-o")
            #self.processus.setArguments(self.path + "dvd")
            #self.processus.setArguments(str(self.filepath))
            self.processus.readyReadStandardError.connect(self.readStdErr)
            self.processus.readyReadStandardOutput.connect(self.readStdOut)
            #unification des deux sorties
            self.processus.setProcessChannelMode(1)
            #run the processus
            self.processus.start(command)
            #if processus is finished run the second methode
            self.processus.finished.connect(self.dvdauthor2)
            #create a path for the filelog
            self.filelogpath = self.path + "dvd.log"
            #create the logfile
            self.filelog = open('self.filelogpath', 'w')
            #self.count = 0
            #activation of the button cancel
            self.ui.btncancel.setEnabled(True)
        else:
            self.ui.textEdit.append("Please choose one file and one action...")

    #===================================================================================================================
    def cancel(self):
        self.processus.kill()
        self.workfinished()

    #===================================================================================================================
    def workfinished(self):
        self.ui.progressbarexport.reset()
        self.ui.btncancel.setEnabled(False)
        self.ui.btnexport.setEnabled(True)
        self.ui.chkvideofile.setEnabled(False)
        self.ui.chkimageiso.setEnabled(False)

    #===================================================================================================================
    def readStdErr(self):
        self.linerr = str(self.processus.readLineStderr())
        self.ui.textEdit.append(self.linerr)
        self.filelog.write(self.linerr)
        if self.count == 100:
            self.count = 0
        self.count = self.count + 1
        self.ui.progressbarexport.setProgress(self.count)

    #===================================================================================================================
    def readStdOut(self):
        self.lineout = str(self.processus.readLineStdout())
        self.ui.textEdit.append(self.lineout)
        self.filelog.write(self.lineout)
        if self.count == 100:
            self.count = 0
        self.count = self.count + 1
        self.ui.progressbarexport.setProgress(self.count)

    #===================================================================================================================
    def dvdauthor2(self):
        self.ui.textEdit.append("**** dvdauthor : PROCESSUS 2 ****")
        #command = ["dvdauthor", "-T", "-o", "(self.path + 'dvd')"]
        command = ["tcprobe", "-i", "self.path"]
        self.processus = QProcess()
        self.processus.setArguments(command)
        #self.processus.setArguments("dvdauthor")
        #self.processus.setArguments("-T")
        #self.processus.setArguments("-o")
        #self.processus.setArguments(self.path + "dvd")
        self.processus.readyReadStandardError.connect(self.readStderr)
        self.processus.readyReadStandardOutput.connect(self.readStdOut)
        if self.ui.chkimageiso.isChecked():
            self.processus.finished.connect(self.dvdiso)
        else:
            self.processus.finished.connect(self.workfinished)
        self.processus.start()

    #===================================================================================================================
    def dvdiso(self):
        self.ui.textEdit.append("**** mkisofs : PROCESSING ****")
        #command = ["mkisofs", "-o", "(self.path + str(self.ui.lnenamedvd() + '.iso')", "-V", "self.lnenamedvd.text()", "-dvd-video", "(self.path + 'dvd')"]
        command = ["tcmodinfo", "-p"]
        self.processus = QProcess()
        self.processus.setArguments(command)
        #self.processus.setArguments("mkisofs")
        #self.processus.setArguments("-o")
        #self.processus.setArguments(self.path + str(self.ui.lnenamedvd.text()) + ".iso")
        #self.processus.setArguments("-V")
        #self.processus.setArguments(self.lnenamedvd.text())
        #self.processus.setArguments("-dvd-video")
        #self.processus.setArgument(self.path + "dvd")
        self.processus.readyReadStandardError.connect(self.readStdErr)
        self.processus.readyReadStandardOutput.connect(self.readStdOut)
        self.processus.finished.connect(self.workfinished)
        self.processus.start()

    #===================================================================================================================
    def UpdateProgressBar(self):
        while self.processus.Running():
            for i in range(0, 100):
                self.ui.progressbarexport.setProgress(i)
            self.ui.progressbarexport.reset()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    KvIso = KvIso()
    KvIso.show()
    application.exec_()
