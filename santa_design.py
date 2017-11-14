# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'santa_design.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 452)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.buttonWidget = QtWidgets.QWidget(MainWindow)
        self.buttonWidget.setAutoFillBackground(True)
        self.buttonWidget.setStyleSheet("")
        self.buttonWidget.setObjectName("buttonWidget")
        self.btnChooseSanta = QtWidgets.QPushButton(self.buttonWidget)
        self.btnChooseSanta.setGeometry(QtCore.QRect(270, 250, 312, 111))
        self.btnChooseSanta.setAutoFillBackground(False)
        self.btnChooseSanta.setStyleSheet("background-color: rgb(69, 94, 84);\n"
"border-width: 3px;\n"
"border-style:solid;\n"
"border-radius: 15px;\n"
"border-color: rgb(207, 144, 90);\n"
"font: bold 24px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"color: rgb(211, 215, 207);")
        self.btnChooseSanta.setObjectName("btnChooseSanta")
        self.lblDasher = QtWidgets.QLabel(self.buttonWidget)
        self.lblDasher.setGeometry(QtCore.QRect(250, 30, 350, 250))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDasher.sizePolicy().hasHeightForWidth())
        self.lblDasher.setSizePolicy(sizePolicy)
        self.lblDasher.setStyleSheet("")
        self.lblDasher.setObjectName("lblDasher")
        self.lblVixen = QtWidgets.QLabel(self.buttonWidget)
        self.lblVixen.setGeometry(QtCore.QRect(-10, 210, 350, 250))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblVixen.sizePolicy().hasHeightForWidth())
        self.lblVixen.setSizePolicy(sizePolicy)
        self.lblVixen.setStyleSheet("")
        self.lblVixen.setObjectName("lblVixen")
        self.Background = QtWidgets.QLabel(self.buttonWidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 641, 461))
        self.Background.setStyleSheet("background-image: url(./bg.jpg);\n"
"background-repeat: repeat-xy;\n"
"background-size: 50%;")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.Background.raise_()
        self.lblVixen.raise_()
        self.btnChooseSanta.raise_()
        self.lblDasher.raise_()
        MainWindow.setCentralWidget(self.buttonWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnChooseSanta.setText(_translate("MainWindow", "Генериране на Дядовци"))
        self.lblDasher.setText(_translate("MainWindow", "Dasher"))
        self.lblVixen.setText(_translate("MainWindow", "VIxen"))

