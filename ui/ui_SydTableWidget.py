# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SydTableWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SydTableWidget(object):
    def setupUi(self, SydTableWidget):
        if not SydTableWidget.objectName():
            SydTableWidget.setObjectName(u"SydTableWidget")
        SydTableWidget.resize(1277, 606)
        self.verticalLayout = QVBoxLayout(SydTableWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SydTableWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.edit_filter = QLineEdit(SydTableWidget)
        self.edit_filter.setObjectName(u"edit_filter")
        self.edit_filter.setMinimumSize(QSize(200, 0))
        self.edit_filter.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.edit_filter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table_view = QTableView(SydTableWidget)
        self.table_view.setObjectName(u"table_view")

        self.verticalLayout.addWidget(self.table_view)


        self.retranslateUi(SydTableWidget)

        QMetaObject.connectSlotsByName(SydTableWidget)
    # setupUi

    def retranslateUi(self, SydTableWidget):
        SydTableWidget.setWindowTitle(QCoreApplication.translate("SydTableWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("SydTableWidget", u"Filter :", None))
    # retranslateUi

