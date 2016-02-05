# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QDvgrab.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/camera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbldescriptioncamecorder = QtWidgets.QLabel(self.centralwidget)
        self.lbldescriptioncamecorder.setGeometry(QtCore.QRect(30, 50, 250, 20))
        self.lbldescriptioncamecorder.setObjectName("lbldescriptioncamecorder")
        self.lblcamcorder = QtWidgets.QLabel(self.centralwidget)
        self.lblcamcorder.setGeometry(QtCore.QRect(320, 50, 250, 20))
        self.lblcamcorder.setObjectName("lblcamcorder")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 100, 250, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 150, 90, 14))
        self.label_2.setObjectName("label_2")
        self.lblfree = QtWidgets.QLabel(self.centralwidget)
        self.lblfree.setGeometry(QtCore.QRect(360, 150, 90, 14))
        self.lblfree.setObjectName("lblfree")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 190, 90, 14))
        self.label_4.setObjectName("label_4")
        self.lblused = QtWidgets.QLabel(self.centralwidget)
        self.lblused.setGeometry(QtCore.QRect(360, 190, 90, 14))
        self.lblused.setObjectName("lblused")
        self.lbltotal = QtWidgets.QLabel(self.centralwidget)
        self.lbltotal.setGeometry(QtCore.QRect(70, 220, 450, 20))
        self.lbltotal.setObjectName("lbltotal")
        self.progressbaracquisition = QtWidgets.QProgressBar(self.centralwidget)
        self.progressbaracquisition.setGeometry(QtCore.QRect(20, 310, 571, 35))
        self.progressbaracquisition.setProperty("value", 0)
        self.progressbaracquisition.setObjectName("progressbaracquisition")
        self.btnacquisitiondv = QtWidgets.QPushButton(self.centralwidget)
        self.btnacquisitiondv.setGeometry(QtCore.QRect(70, 380, 450, 50))
        self.btnacquisitiondv.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnacquisitiondv.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/media-optical-video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnacquisitiondv.setIcon(icon1)
        self.btnacquisitiondv.setIconSize(QtCore.QSize(48, 48))
        self.btnacquisitiondv.setAutoDefault(False)
        self.btnacquisitiondv.setDefault(False)
        self.btnacquisitiondv.setFlat(False)
        self.btnacquisitiondv.setObjectName("btnacquisitiondv")
        self.btnrecordmpeg = QtWidgets.QPushButton(self.centralwidget)
        self.btnrecordmpeg.setGeometry(QtCore.QRect(70, 470, 450, 50))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../images/tools-media-optical-burn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnrecordmpeg.setIcon(icon2)
        self.btnrecordmpeg.setIconSize(QtCore.QSize(48, 48))
        self.btnrecordmpeg.setObjectName("btnrecordmpeg")
        self.btnstartrecord = QtWidgets.QPushButton(self.centralwidget)
        self.btnstartrecord.setGeometry(QtCore.QRect(70, 560, 200, 45))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../images/media-tape.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnstartrecord.setIcon(icon3)
        self.btnstartrecord.setIconSize(QtCore.QSize(48, 48))
        self.btnstartrecord.setObjectName("btnstartrecord")
        self.btnpreferences = QtWidgets.QPushButton(self.centralwidget)
        self.btnpreferences.setGeometry(QtCore.QRect(320, 560, 200, 45))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../images/tools-wizard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnpreferences.setIcon(icon4)
        self.btnpreferences.setIconSize(QtCore.QSize(48, 48))
        self.btnpreferences.setObjectName("btnpreferences")
        self.btnhelp = QtWidgets.QPushButton(self.centralwidget)
        self.btnhelp.setGeometry(QtCore.QRect(70, 680, 200, 45))
        self.btnhelp.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../images/system-help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnhelp.setIcon(icon5)
        self.btnhelp.setIconSize(QtCore.QSize(48, 48))
        self.btnhelp.setObjectName("btnhelp")
        self.btnquit = QtWidgets.QPushButton(self.centralwidget)
        self.btnquit.setGeometry(QtCore.QRect(350, 680, 200, 45))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../images/application-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnquit.setIcon(icon6)
        self.btnquit.setIconSize(QtCore.QSize(48, 48))
        self.btnquit.setObjectName("btnquit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 230, 20))
        self.label_3.setObjectName("label_3")
        self.lnecapturename = QtWidgets.QLineEdit(self.centralwidget)
        self.lnecapturename.setGeometry(QtCore.QRect(280, 260, 270, 35))
        self.lnecapturename.setObjectName("lnecapturename")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_Directory = QtWidgets.QAction(MainWindow)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout_QdvGrab = QtWidgets.QAction(MainWindow)
        self.actionAbout_QdvGrab.setObjectName("actionAbout_QdvGrab")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionOpen_Directory)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionAbout_QdvGrab)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.btnquit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QDvGrab"))
        self.lbldescriptioncamecorder.setText(_translate("MainWindow", "<html><head/><body><p>DV Camecorder:</p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Montage point</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Free:</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Used:</p></body></html>"))
        self.lbltotal.setText(_translate("MainWindow", "<html><head/><body><p>This Hard drive can around </p></body></html>"))
        self.btnacquisitiondv.setText(_translate("MainWindow", "DV Acquisition"))
        self.btnrecordmpeg.setText(_translate("MainWindow", "Record MPEG"))
        self.btnstartrecord.setText(_translate("MainWindow", "Start Record"))
        self.btnpreferences.setText(_translate("MainWindow", "Preferences"))
        self.btnhelp.setText(_translate("MainWindow", "Help"))
        self.btnquit.setText(_translate("MainWindow", "Quit"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Capture Name:</p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_Directory.setText(_translate("MainWindow", "Open Directory"))
        self.actionOpen_Directory.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionAbout_QdvGrab.setText(_translate("MainWindow", "About QDvGrab"))
        self.actionAbout_QdvGrab.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
        self.actionAbout_Qt.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

