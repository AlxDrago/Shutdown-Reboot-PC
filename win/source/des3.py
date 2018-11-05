# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(412, 245)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 191, 31))
        self.textEdit.setStyleSheet("font-size: 14px;")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(26, 10, 201, 41))
        self.label.setObjectName("label")
        self.checkBoxReboot = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxReboot.setGeometry(QtCore.QRect(30, 100, 191, 23))
        self.checkBoxReboot.setObjectName("checkBoxReboot")
        self.hourInput = QtWidgets.QTextEdit(self.centralwidget)
        self.hourInput.setGeometry(QtCore.QRect(260, 80, 51, 31))
        self.hourInput.setObjectName("hourInput")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(240, 130, 151, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopBtn.sizePolicy().hasHeightForWidth())
        self.stopBtn.setSizePolicy(sizePolicy)
        self.stopBtn.setStyleSheet("background-color: red;")
        self.stopBtn.setObjectName("stopBtn")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.stopBtn)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setEnabled(True)
        self.startBtn.setGeometry(QtCore.QRect(30, 130, 171, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy)
        self.startBtn.setStyleSheet("background-color: green;")
        self.startBtn.setObjectName("startBtn")
        self.buttonGroup_2.addButton(self.startBtn)
        self.minuteInput = QtWidgets.QTextEdit(self.centralwidget)
        self.minuteInput.setGeometry(QtCore.QRect(330, 80, 61, 31))
        self.minuteInput.setObjectName("minuteInput")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 40, 41, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 40, 61, 31))
        self.label_4.setObjectName("label_4")
        self.checkTimeShut = QtWidgets.QCheckBox(self.centralwidget)
        self.checkTimeShut.setGeometry(QtCore.QRect(260, 0, 131, 41))
        self.checkTimeShut.setObjectName("checkTimeShut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 22))
        self.menubar.setObjectName("menubar")
        self.menuShutdownn = QtWidgets.QMenu(self.menubar)
        self.menuShutdownn.setObjectName("menuShutdownn")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuShutdownn.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Задайте время отключения\n"
" в минутах"))
        self.checkBoxReboot.setText(_translate("MainWindow", "Перезагрузить"))
        self.stopBtn.setText(_translate("MainWindow", "Остановить"))
        self.startBtn.setText(_translate("MainWindow", "Включить таймер"))
        self.label_3.setText(_translate("MainWindow", "Часы:"))
        self.label_4.setText(_translate("MainWindow", "Минуты:"))
        self.checkTimeShut.setText(_translate("MainWindow", "Включить по\n"
"времени"))


