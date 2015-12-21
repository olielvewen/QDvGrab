# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credits.ui'
#
# Created: Mon Dec 21 17:02:31 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_creditscreen(object):
    def setupUi(self, creditscreen):
        creditscreen.setObjectName("creditscreen")
        creditscreen.resize(400, 300)
        creditscreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.verticalLayout = QtWidgets.QVBoxLayout(creditscreen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(creditscreen)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_2.addWidget(self.textBrowser_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_3.addWidget(self.textBrowser_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_4.addWidget(self.textBrowser_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_5.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(258, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnclose = QtWidgets.QPushButton(creditscreen)
        self.btnclose.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.btnclose.setObjectName("btnclose")
        self.horizontalLayout.addWidget(self.btnclose)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(creditscreen)
        self.tabWidget.setCurrentIndex(0)
        self.btnclose.clicked.connect(creditscreen.reject)
        QtCore.QMetaObject.connectSlotsByName(creditscreen)

    def retranslateUi(self, creditscreen):
        _translate = QtCore.QCoreApplication.translate
        creditscreen.setWindowTitle(_translate("creditscreen", "Dialog"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("creditscreen", "Written by"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("creditscreen", "Documented by"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("creditscreen", "Translated by"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("creditscreen", "License"))
        self.btnclose.setText(_translate("creditscreen", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    creditscreen = QtWidgets.QDialog()
    ui = Ui_creditscreen()
    ui.setupUi(creditscreen)
    creditscreen.show()
    sys.exit(app.exec_())

