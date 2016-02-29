#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

import sys

if __name__ == "__main__":

    #we are going into the work folder of the project
    project_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_path)
    os.chdir(project_path)

    #we are making all other paths
    locale_path = os.path.join(project_path, 'src', 'locale')
    classes_path = os.path.join(project_path, 'src', 'classes')
    images_path = os.path.join(project_path, 'src', 'images')
    ui_path = os.path.join(project_path, 'src', 'ui')
    windows_path = os.path.join(project_path, 'src','windows')
    license_path = os.path.dirname(os.path.abspath('LICENSE'))

    #we are making qdvgrab folder in user home
    #user_folder = QDir.homePath()
    #configFolder = os.path.join(QDir.homePath(), ".qdvgrab")
    #configFile = os.path.join(QDir.homePath(), ".qdvgrab/config.conf")
    #configLog = os.path.join(QDir.homePath(), ".qdvgrab/logfile")

    #we are creating a basic config file


#we start the gui
try:
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
except ImportError:
    print("unable to import PyQt5 - you should install it if you want an functional version of qdvgrab")
    sys.exit(1)

try:
    from src.ui.qdvgrabui import Ui_MainWindow
    from src.ui.qdvgrab import QdvGrab
    from src.windows.qdvgrab import QdvGrab
except ImportError:
    print("unable to load main file of QDvGrab - an error is came")
    sys.exit(1)

#We launch the GUI
application = QApplication(sys.argv)
QdvGrab = QdvGrab()
QdvGrab.show()
sys.exit(application.exec_())

