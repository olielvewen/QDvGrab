# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kviso.ui'
#
# Created: Tue Aug 12 13:58:09 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_kvisodialog(object):
    def setupUi(self, kvisodialog):
        kvisodialog.setObjectName("kvisodialog")
        kvisodialog.resize(620, 700)
        kvisodialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.frame = QtWidgets.QFrame(kvisodialog)
        self.frame.setGeometry(QtCore.QRect(10, 10, 601, 671))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnhelp = QtWidgets.QPushButton(self.frame)
        self.btnhelp.setGeometry(QtCore.QRect(390, 30, 180, 45))
        self.btnhelp.setObjectName("btnhelp")
        self.btnchoosevideofile = QtWidgets.QPushButton(self.frame)
        self.btnchoosevideofile.setGeometry(QtCore.QRect(20, 100, 330, 50))
        self.btnchoosevideofile.setIconSize(QtCore.QSize(24, 24))
        self.btnchoosevideofile.setObjectName("btnchoosevideofile")
        self.btnquit = QtWidgets.QPushButton(self.frame)
        self.btnquit.setGeometry(QtCore.QRect(400, 270, 180, 45))
        self.btnquit.setObjectName("btnquit")
        self.btnexport = QtWidgets.QPushButton(self.frame)
        self.btnexport.setGeometry(QtCore.QRect(20, 270, 180, 45))
        self.btnexport.setObjectName("btnexport")
        self.btncancel = QtWidgets.QPushButton(self.frame)
        self.btncancel.setGeometry(QtCore.QRect(210, 270, 180, 45))
        self.btncancel.setObjectName("btncancel")
        self.chkvideofile = QtWidgets.QCheckBox(self.frame)
        self.chkvideofile.setGeometry(QtCore.QRect(20, 160, 280, 35))
        self.chkvideofile.setObjectName("chkvideofile")
        self.chkimageiso = QtWidgets.QCheckBox(self.frame)
        self.chkimageiso.setGeometry(QtCore.QRect(20, 210, 280, 35))
        self.chkimageiso.setObjectName("chkimageiso")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 40, 320, 35))
        self.label.setObjectName("label")
        self.progressbarexport = QtWidgets.QProgressBar(self.frame)
        self.progressbarexport.setGeometry(QtCore.QRect(20, 340, 571, 35))
        self.progressbarexport.setProperty("value", 0)
        self.progressbarexport.setObjectName("progressbarexport")
        self.framelog = QtWidgets.QFrame(self.frame)
        self.framelog.setGeometry(QtCore.QRect(20, 400, 571, 251))
        self.framelog.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framelog.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framelog.setObjectName("framelog")
        self.textEdit = QtWidgets.QTextEdit(self.framelog)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 571, 251))
        self.textEdit.setObjectName("textEdit")
        self.lnenamedvd = QtWidgets.QLineEdit(self.frame)
        self.lnenamedvd.setGeometry(QtCore.QRect(330, 210, 250, 35))
        self.lnenamedvd.setObjectName("lnenamedvd")

        self.retranslateUi(kvisodialog)
        QtCore.QMetaObject.connectSlotsByName(kvisodialog)

    def retranslateUi(self, kvisodialog):
        _translate = QtCore.QCoreApplication.translate
        kvisodialog.setWindowTitle(_translate("kvisodialog", "KViso"))
        self.btnhelp.setText(_translate("kvisodialog", "Help"))
        self.btnchoosevideofile.setText(_translate("kvisodialog", "Choose a Video File"))
        self.btnquit.setText(_translate("kvisodialog", "Quit"))
        self.btnexport.setText(_translate("kvisodialog", "Export"))
        self.btncancel.setText(_translate("kvisodialog", "Cancel"))
        self.chkvideofile.setText(_translate("kvisodialog", "Create Video Files"))
        self.chkimageiso.setText(_translate("kvisodialog", "Create image ISO"))
        self.label.setText(_translate("kvisodialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Create your ISO with a MPEG File</span></p></body></html>"))
        self.lnenamedvd.setText(_translate("kvisodialog", "Dvd Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kvisodialog = QtWidgets.QDialog()
    ui = Ui_kvisodialog()
    ui.setupUi(kvisodialog)
    kvisodialog.show()
    sys.exit(app.exec_())

