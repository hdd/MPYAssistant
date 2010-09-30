# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIAssistant.ui'
#
# Created: Fri Oct  1 00:34:50 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(497, 543)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.CB_pluginTipe = QtGui.QComboBox(self.tab)
        self.CB_pluginTipe.setObjectName("CB_pluginTipe")
        self.CB_pluginTipe.addItem("")
        self.CB_pluginTipe.addItem("")
        self.CB_pluginTipe.addItem("")
        self.gridLayout.addWidget(self.CB_pluginTipe, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.TX_pluginName = QtGui.QLineEdit(self.tab)
        self.TX_pluginName.setObjectName("TX_pluginName")
        self.gridLayout.addWidget(self.TX_pluginName, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.TX_authorName = QtGui.QLineEdit(self.tab)
        self.TX_authorName.setObjectName("TX_authorName")
        self.gridLayout.addWidget(self.TX_authorName, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.CB_pluginId = QtGui.QComboBox(self.tab)
        self.CB_pluginId.setEditable(True)
        self.CB_pluginId.setObjectName("CB_pluginId")
        self.CB_pluginId.addItem("")
        self.CB_pluginId.addItem("")
        self.CB_pluginId.addItem("")
        self.gridLayout.addWidget(self.CB_pluginId, 3, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.TX_description = QtGui.QPlainTextEdit(self.tab)
        self.TX_description.setObjectName("TX_description")
        self.gridLayout.addWidget(self.TX_description, 4, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 411, 111))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.BT_generate = QtGui.QPushButton(Dialog)
        self.BT_generate.setObjectName("BT_generate")
        self.verticalLayout.addWidget(self.BT_generate)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Maya Python Plugins Assistant</p></td></tr></table></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Plugin Type", None, QtGui.QApplication.UnicodeUTF8))
        self.CB_pluginTipe.setItemText(0, QtGui.QApplication.translate("Dialog", "Simple Maya Node", None, QtGui.QApplication.UnicodeUTF8))
        self.CB_pluginTipe.setItemText(1, QtGui.QApplication.translate("Dialog", "Deformer Node", None, QtGui.QApplication.UnicodeUTF8))
        self.CB_pluginTipe.setItemText(2, QtGui.QApplication.translate("Dialog", "Command", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Plugin Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Author Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Plugin Id", None, QtGui.QApplication.UnicodeUTF8))
        self.CB_pluginId.setItemText(0, QtGui.QApplication.translate("Dialog", "0x87005", None, QtGui.QApplication.UnicodeUTF8))
        self.CB_pluginId.setItemText(1, QtGui.QApplication.translate("Dialog", "0x8700B", None, QtGui.QApplication.UnicodeUTF8))
        self.CB_pluginId.setItemText(2, QtGui.QApplication.translate("Dialog", "0x87010", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Basic Informations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Something smart\n"
"the provided nodes ids are taken from the standar maya examples , remember to change them to something unique, before releasing it", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.BT_generate.setText(QtGui.QApplication.translate("Dialog", "Generate", None, QtGui.QApplication.UnicodeUTF8))

