# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'linkCount.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(675, 466)
        self.txtSearch = QtWidgets.QTextEdit(Dialog)
        self.txtSearch.setGeometry(QtCore.QRect(160, 40, 361, 31))
        self.txtSearch.setObjectName("txtSearch")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 45, 151, 21))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.label.setObjectName("label")
        self.btnSearch = QtWidgets.QPushButton(Dialog)
        self.btnSearch.setGeometry(QtCore.QRect(540, 40, 101, 31))
        self.btnSearch.setStyleSheet(".button {\n"
"  background-color: #5555ff;\n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;\n"
"  margin: 4px 2px;\n"
"  cursor: pointer;\n"
"}")
        self.btnSearch.setObjectName("btnSearch")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 611, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter You Link"))
        self.btnSearch.setText(_translate("Dialog", "Search"))

