# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_results.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(621, 454)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.btnClean = QtWidgets.QPushButton(Form)
        self.btnClean.setGeometry(QtCore.QRect(240, 350, 191, 51))
        self.btnClean.setObjectName("btnClean")
        self.wgtParticipants = QtWidgets.QListWidget(Form)
        self.wgtParticipants.setGeometry(QtCore.QRect(30, 20, 291, 191))
        self.wgtParticipants.setObjectName("wgtParticipants")
        self.btnShow = QtWidgets.QPushButton(Form)
        self.btnShow.setGeometry(QtCore.QRect(330, 40, 271, 71))
        self.btnShow.setObjectName("btnShow")
        self.lblSanta = QtWidgets.QLabel(Form)
        self.lblSanta.setGeometry(QtCore.QRect(30, 220, 511, 101))
        self.lblSanta.setObjectName("lblSanta")
        self.btnSend = QtWidgets.QPushButton(Form)
        self.btnSend.setGeometry(QtCore.QRect(330, 130, 271, 71))
        self.btnSend.setObjectName("btnSend")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnClean.setText(_translate("Form", "Зачисти"))
        self.btnShow.setText(_translate("Form", "Покажи дядото ми"))
        self.lblSanta.setText(_translate("Form", "TextLabel"))
        self.btnSend.setText(_translate("Form", "Прати ми имейл с дядо"))

