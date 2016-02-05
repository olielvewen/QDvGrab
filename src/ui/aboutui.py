# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutscreen(object):
    def setupUi(self, aboutscreen):
        aboutscreen.setObjectName("aboutscreen")
        aboutscreen.resize(550, 450)
        aboutscreen.setMaximumSize(QtCore.QSize(550, 450))
        aboutscreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        aboutscreen.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(aboutscreen)
        self.verticalLayout_2.setContentsMargins(9, 50, -1, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblimageicon = QtWidgets.QLabel(aboutscreen)
        self.lblimageicon.setMinimumSize(QtCore.QSize(221, 281))
        self.lblimageicon.setObjectName("lblimageicon")
        self.horizontalLayout_2.addWidget(self.lblimageicon)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblprojectname = QtWidgets.QLabel(aboutscreen)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Armenian")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblprojectname.setFont(font)
        self.lblprojectname.setObjectName("lblprojectname")
        self.verticalLayout.addWidget(self.lblprojectname)
        self.lblresume = QtWidgets.QLabel(aboutscreen)
        self.lblresume.setMinimumSize(QtCore.QSize(240, 240))
        self.lblresume.setObjectName("lblresume")
        self.verticalLayout.addWidget(self.lblresume)
        self.lblversionplateform = QtWidgets.QLabel(aboutscreen)
        self.lblversionplateform.setMinimumSize(QtCore.QSize(240, 37))
        self.lblversionplateform.setObjectName("lblversionplateform")
        self.verticalLayout.addWidget(self.lblversionplateform)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btncredits = QtWidgets.QPushButton(aboutscreen)
        self.btncredits.setMinimumSize(QtCore.QSize(130, 35))
        self.btncredits.setObjectName("btncredits")
        self.horizontalLayout.addWidget(self.btncredits)
        spacerItem = QtWidgets.QSpacerItem(258, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnclose = QtWidgets.QPushButton(aboutscreen)
        self.btnclose.setMinimumSize(QtCore.QSize(130, 35))
        self.btnclose.setObjectName("btnclose")
        self.horizontalLayout.addWidget(self.btnclose)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(aboutscreen)
        self.btnclose.clicked.connect(aboutscreen.reject)
        QtCore.QMetaObject.connectSlotsByName(aboutscreen)

    def retranslateUi(self, aboutscreen):
        _translate = QtCore.QCoreApplication.translate
        aboutscreen.setWindowTitle(_translate("aboutscreen", "About"))
        self.lblresume.setText(_translate("aboutscreen", "<html><head/><body><p>Gui for grabbing film from an DV or HDV </p><p>Camecorder in the simpliest way on the </p><p>Hard Drive.</p><p><br/></p><p>QDvGrab - <a href=\"https://github.com/olielvewen/QDvGrab\"><span style=\" text-decoration: underline; color:#0000ff;\">Home Page</span></a></p><p><a href=\"https://github.com/olielvewen/QDvGrab\"><span style=\" text-decoration: underline; color:#000000;\">Copyright 2014-2016 Olivier Girard</span></a><br/><a href=\"https://github.com/olielvewen/QDvGrab\"><span style=\" text-decoration: underline; color:#000000;\">License: GNU GPL v3</span></a></p></body></html>"))
        self.btncredits.setText(_translate("aboutscreen", "Credits"))
        self.btnclose.setText(_translate("aboutscreen", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutscreen = QtWidgets.QDialog()
    ui = Ui_aboutscreen()
    ui.setupUi(aboutscreen)
    aboutscreen.show()
    sys.exit(app.exec_())

