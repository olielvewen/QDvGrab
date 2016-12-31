# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credits.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_creditscreen(object):
    def setupUi(self, creditscreen):
        creditscreen.setObjectName("creditscreen")
        creditscreen.resize(700, 480)
        creditscreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        creditscreen.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(creditscreen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(creditscreen)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowserwritten = QtWidgets.QTextBrowser(self.tab)
        self.textBrowserwritten.setObjectName("textBrowserwritten")
        self.verticalLayout_2.addWidget(self.textBrowserwritten)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowserdocumented = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowserdocumented.setObjectName("textBrowserdocumented")
        self.horizontalLayout_3.addWidget(self.textBrowserdocumented)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowsertranslated = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowsertranslated.setObjectName("textBrowsertranslated")
        self.horizontalLayout_4.addWidget(self.textBrowsertranslated)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowserlicense = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowserlicense.setObjectName("textBrowserlicense")
        self.horizontalLayout_5.addWidget(self.textBrowserlicense)
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
        creditscreen.setWindowTitle(_translate("creditscreen", "Credits"))
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

