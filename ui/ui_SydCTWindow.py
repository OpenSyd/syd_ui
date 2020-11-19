# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SydCTWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SydCTWindow(object):
    def setupUi(self, SydCTWindow):
        if not SydCTWindow.objectName():
            SydCTWindow.setObjectName(u"SydCTWindow")
        SydCTWindow.resize(400, 300)
        self.button_ct_on = QPushButton(SydCTWindow)
        self.button_ct_on.setObjectName(u"button_ct_on")
        self.button_ct_on.setGeometry(QRect(150, 60, 111, 25))
        self.button_ct_off = QPushButton(SydCTWindow)
        self.button_ct_off.setObjectName(u"button_ct_off")
        self.button_ct_off.setGeometry(QRect(150, 150, 121, 25))

        self.retranslateUi(SydCTWindow)

        QMetaObject.connectSlotsByName(SydCTWindow)
    # setupUi

    def retranslateUi(self, SydCTWindow):
        SydCTWindow.setWindowTitle(QCoreApplication.translate("SydCTWindow", u"CTWindow", None))
        self.button_ct_on.setText(QCoreApplication.translate("SydCTWindow", u"View with CT", None))
        self.button_ct_off.setText(QCoreApplication.translate("SydCTWindow", u"View without CT", None))
    # retranslateUi

