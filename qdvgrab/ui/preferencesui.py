# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(603, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/camera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabgeneral = QtWidgets.QWidget()
        self.tabgeneral.setObjectName("tabgeneral")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabgeneral)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbogeneral = QtWidgets.QGroupBox(self.tabgeneral)
        self.gbogeneral.setObjectName("gbogeneral")
        self.gridLayout = QtWidgets.QGridLayout(self.gbogeneral)
        self.gridLayout.setObjectName("gridLayout")
        self.txtlanguagues = QtWidgets.QLabel(self.gbogeneral)
        self.txtlanguagues.setObjectName("txtlanguagues")
        self.gridLayout.addWidget(self.txtlanguagues, 0, 0, 1, 1)
        self.cmblanguages = QtWidgets.QComboBox(self.gbogeneral)
        self.cmblanguages.setMinimumSize(QtCore.QSize(380, 35))
        self.cmblanguages.setObjectName("cmblanguages")
        self.gridLayout.addWidget(self.cmblanguages, 0, 1, 1, 2)
        self.txtoutputfile = QtWidgets.QLabel(self.gbogeneral)
        self.txtoutputfile.setObjectName("txtoutputfile")
        self.gridLayout.addWidget(self.txtoutputfile, 1, 0, 1, 1)
        self.lneoutputfile = QtWidgets.QLineEdit(self.gbogeneral)
        self.lneoutputfile.setMinimumSize(QtCore.QSize(230, 35))
        self.lneoutputfile.setObjectName("lneoutputfile")
        self.gridLayout.addWidget(self.lneoutputfile, 1, 1, 1, 1)
        self.btnchoosefile = QtWidgets.QPushButton(self.gbogeneral)
        self.btnchoosefile.setMinimumSize(QtCore.QSize(130, 35))
        self.btnchoosefile.setObjectName("btnchoosefile")
        self.gridLayout.addWidget(self.btnchoosefile, 1, 2, 1, 1)
        self.txtnamecamcorder = QtWidgets.QLabel(self.gbogeneral)
        self.txtnamecamcorder.setObjectName("txtnamecamcorder")
        self.gridLayout.addWidget(self.txtnamecamcorder, 2, 0, 1, 1)
        self.lnenamecamcorder = QtWidgets.QLineEdit(self.gbogeneral)
        self.lnenamecamcorder.setMinimumSize(QtCore.QSize(380, 35))
        self.lnenamecamcorder.setObjectName("lnenamecamcorder")
        self.gridLayout.addWidget(self.lnenamecamcorder, 2, 1, 1, 2)
        self.verticalLayout.addWidget(self.gbogeneral)
        self.gbodependances = QtWidgets.QGroupBox(self.tabgeneral)
        self.gbodependances.setObjectName("gbodependances")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gbodependances)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbldvgrab = QtWidgets.QLabel(self.gbodependances)
        self.lbldvgrab.setObjectName("lbldvgrab")
        self.gridLayout_2.addWidget(self.lbldvgrab, 0, 0, 1, 1)
        self.lnedvgrab = QtWidgets.QLineEdit(self.gbodependances)
        self.lnedvgrab.setMinimumSize(QtCore.QSize(230, 35))
        self.lnedvgrab.setObjectName("lnedvgrab")
        self.gridLayout_2.addWidget(self.lnedvgrab, 0, 1, 1, 1)
        self.btndvgrab = QtWidgets.QPushButton(self.gbodependances)
        self.btndvgrab.setMinimumSize(QtCore.QSize(130, 35))
        self.btndvgrab.setObjectName("btndvgrab")
        self.gridLayout_2.addWidget(self.btndvgrab, 0, 2, 1, 1)
        self.lbltranscode = QtWidgets.QLabel(self.gbodependances)
        self.lbltranscode.setEnabled(True)
        self.lbltranscode.setObjectName("lbltranscode")
        self.gridLayout_2.addWidget(self.lbltranscode, 1, 0, 1, 1)
        self.lnetranscode = QtWidgets.QLineEdit(self.gbodependances)
        self.lnetranscode.setEnabled(True)
        self.lnetranscode.setMinimumSize(QtCore.QSize(230, 35))
        self.lnetranscode.setObjectName("lnetranscode")
        self.gridLayout_2.addWidget(self.lnetranscode, 1, 1, 1, 1)
        self.btntranscode = QtWidgets.QPushButton(self.gbodependances)
        self.btntranscode.setMinimumSize(QtCore.QSize(130, 35))
        self.btntranscode.setObjectName("btntranscode")
        self.gridLayout_2.addWidget(self.btntranscode, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.gbodependances)
        self.tabWidget.addTab(self.tabgeneral, "")
        self.tabconversion = QtWidgets.QWidget()
        self.tabconversion.setMinimumSize(QtCore.QSize(577, 568))
        self.tabconversion.setObjectName("tabconversion")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tabconversion)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gboformatcapture = QtWidgets.QGroupBox(self.tabconversion)
        self.gboformatcapture.setMinimumSize(QtCore.QSize(551, 181))
        self.gboformatcapture.setObjectName("gboformatcapture")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.gboformatcapture)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblformats = QtWidgets.QLabel(self.gboformatcapture)
        self.lblformats.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblformats.sizePolicy().hasHeightForWidth())
        self.lblformats.setSizePolicy(sizePolicy)
        self.lblformats.setMinimumSize(QtCore.QSize(94, 35))
        self.lblformats.setObjectName("lblformats")
        self.horizontalLayout_4.addWidget(self.lblformats)
        self.cmbformatcapture = QtWidgets.QComboBox(self.gboformatcapture)
        self.cmbformatcapture.setMinimumSize(QtCore.QSize(434, 35))
        self.cmbformatcapture.setObjectName("cmbformatcapture")
        self.horizontalLayout_4.addWidget(self.cmbformatcapture)
        self.verticalLayout_9.addWidget(self.gboformatcapture)
        self.gboautomatic = QtWidgets.QGroupBox(self.tabconversion)
        self.gboautomatic.setObjectName("gboautomatic")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gboautomatic)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chknone = QtWidgets.QCheckBox(self.gboautomatic)
        self.chknone.setObjectName("chknone")
        self.verticalLayout_2.addWidget(self.chknone)
        self.chkdvraw = QtWidgets.QCheckBox(self.gboautomatic)
        self.chkdvraw.setObjectName("chkdvraw")
        self.verticalLayout_2.addWidget(self.chkdvraw)
        self.chkdv2 = QtWidgets.QCheckBox(self.gboautomatic)
        self.chkdv2.setObjectName("chkdv2")
        self.verticalLayout_2.addWidget(self.chkdv2)
        self.chkhdv = QtWidgets.QCheckBox(self.gboautomatic)
        self.chkhdv.setObjectName("chkhdv")
        self.verticalLayout_2.addWidget(self.chkhdv)
        self.verticalLayout_9.addWidget(self.gboautomatic)
        self.gbodetectionscene = QtWidgets.QGroupBox(self.tabconversion)
        self.gbodetectionscene.setMinimumSize(QtCore.QSize(551, 151))
        self.gbodetectionscene.setObjectName("gbodetectionscene")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gbodetectionscene)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.chkdetection = QtWidgets.QCheckBox(self.gbodetectionscene)
        self.chkdetection.setMinimumSize(QtCore.QSize(470, 25))
        self.chkdetection.setObjectName("chkdetection")
        self.verticalLayout_4.addWidget(self.chkdetection)
        self.chkautomatic = QtWidgets.QCheckBox(self.gbodetectionscene)
        self.chkautomatic.setMinimumSize(QtCore.QSize(470, 25))
        self.chkautomatic.setObjectName("chkautomatic")
        self.verticalLayout_4.addWidget(self.chkautomatic)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkscene = QtWidgets.QCheckBox(self.gbodetectionscene)
        self.chkscene.setMinimumSize(QtCore.QSize(170, 25))
        self.chkscene.setObjectName("chkscene")
        self.horizontalLayout.addWidget(self.chkscene)
        self.spbscene = QtWidgets.QSpinBox(self.gbodetectionscene)
        self.spbscene.setMinimumSize(QtCore.QSize(120, 30))
        self.spbscene.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spbscene.setObjectName("spbscene")
        self.horizontalLayout.addWidget(self.spbscene)
        self.label_3 = QtWidgets.QLabel(self.gbodetectionscene)
        self.label_3.setMinimumSize(QtCore.QSize(170, 25))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_9.addWidget(self.gbodetectionscene)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tabconversion, "")
        self.tabcapture = QtWidgets.QWidget()
        self.tabcapture.setMinimumSize(QtCore.QSize(577, 568))
        self.tabcapture.setObjectName("tabcapture")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tabcapture)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gbocapture = QtWidgets.QGroupBox(self.tabcapture)
        self.gbocapture.setMinimumSize(QtCore.QSize(551, 191))
        self.gbocapture.setObjectName("gbocapture")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.gbocapture)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.chkautomaticrecord = QtWidgets.QCheckBox(self.gbocapture)
        self.chkautomaticrecord.setMinimumSize(QtCore.QSize(470, 25))
        self.chkautomaticrecord.setObjectName("chkautomaticrecord")
        self.verticalLayout_6.addWidget(self.chkautomaticrecord)
        self.chkmanualrecord = QtWidgets.QCheckBox(self.gbocapture)
        self.chkmanualrecord.setMinimumSize(QtCore.QSize(470, 25))
        self.chkmanualrecord.setObjectName("chkmanualrecord")
        self.verticalLayout_6.addWidget(self.chkmanualrecord)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lnehours = QtWidgets.QLineEdit(self.gbocapture)
        self.lnehours.setMinimumSize(QtCore.QSize(110, 25))
        self.lnehours.setObjectName("lnehours")
        self.horizontalLayout_2.addWidget(self.lnehours)
        self.label_4 = QtWidgets.QLabel(self.gbocapture)
        self.label_4.setMinimumSize(QtCore.QSize(60, 20))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lneminutes = QtWidgets.QLineEdit(self.gbocapture)
        self.lneminutes.setMinimumSize(QtCore.QSize(110, 25))
        self.lneminutes.setObjectName("lneminutes")
        self.horizontalLayout_2.addWidget(self.lneminutes)
        self.label_5 = QtWidgets.QLabel(self.gbocapture)
        self.label_5.setMinimumSize(QtCore.QSize(80, 20))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.verticalLayout_11.addWidget(self.gbocapture)
        self.gboplayer = QtWidgets.QGroupBox(self.tabcapture)
        self.gboplayer.setMinimumSize(QtCore.QSize(551, 151))
        self.gboplayer.setTitle("")
        self.gboplayer.setObjectName("gboplayer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gboplayer)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_11.addWidget(self.gboplayer)
        self.tabWidget.addTab(self.tabcapture, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btncredits = QtWidgets.QPushButton(Dialog)
        self.btncredits.setMinimumSize(QtCore.QSize(160, 40))
        self.btncredits.setObjectName("btncredits")
        self.horizontalLayout_3.addWidget(self.btncredits)
        self.btncancel_2 = QtWidgets.QPushButton(Dialog)
        self.btncancel_2.setEnabled(False)
        self.btncancel_2.setFlat(True)
        self.btncancel_2.setObjectName("btncancel_2")
        self.horizontalLayout_3.addWidget(self.btncancel_2)
        self.btncancel = QtWidgets.QPushButton(Dialog)
        self.btncancel.setMinimumSize(QtCore.QSize(160, 40))
        self.btncancel.setObjectName("btncancel")
        self.horizontalLayout_3.addWidget(self.btncancel)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.btncancel.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Preferences"))
        self.gbogeneral.setTitle(_translate("Dialog", "General"))
        self.txtlanguagues.setText(_translate("Dialog", "<html><head/><body><p>Languages:</p></body></html>"))
        self.txtoutputfile.setText(_translate("Dialog", "<html><head/><body><p>Output File:</p></body></html>"))
        self.btnchoosefile.setText(_translate("Dialog", "..."))
        self.txtnamecamcorder.setText(_translate("Dialog", "<html><head/><body><p>Name Camcorder:</p></body></html>"))
        self.gbodependances.setTitle(_translate("Dialog", "Dependencies"))
        self.lbldvgrab.setText(_translate("Dialog", "<html><head/><body><p>DvGrab:</p></body></html>"))
        self.btndvgrab.setText(_translate("Dialog", "..."))
        self.lbltranscode.setText(_translate("Dialog", "<html><head/><body><p>Transcode:</p></body></html>"))
        self.btntranscode.setText(_translate("Dialog", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabgeneral), _translate("Dialog", "General"))
        self.gboformatcapture.setTitle(_translate("Dialog", "Format Capture"))
        self.lblformats.setText(_translate("Dialog", "<html><head/><body><p>Format Capture:</p></body></html>"))
        self.gboautomatic.setTitle(_translate("Dialog", "Automatic Conversion in mpeg2"))
        self.chknone.setText(_translate("Dialog", "None"))
        self.chkdvraw.setText(_translate("Dialog", "DvRaw"))
        self.chkdv2.setText(_translate("Dialog", "DV 2"))
        self.chkhdv.setText(_translate("Dialog", "Hdv"))
        self.gbodetectionscene.setTitle(_translate("Dialog", "Detection Scene"))
        self.chkdetection.setText(_translate("Dialog", "No detection automatic (1 file only)"))
        self.chkautomatic.setText(_translate("Dialog", "Automatic follow the hour and the date of camcording"))
        self.chkscene.setText(_translate("Dialog", "Create a scene every"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>minutes/seconds</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabconversion), _translate("Dialog", "Conversion"))
        self.gbocapture.setTitle(_translate("Dialog", "Capture"))
        self.chkautomaticrecord.setText(_translate("Dialog", "Stop automatically record if not enought free space disk"))
        self.chkmanualrecord.setText(_translate("Dialog", "Record since"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p>hours</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p>minutes</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabcapture), _translate("Dialog", "Capture"))
        self.btncredits.setText(_translate("Dialog", "Credits"))
        self.btncancel.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
