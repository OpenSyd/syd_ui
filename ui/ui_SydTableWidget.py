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
        SydTableWidget.resize(1008, 668)
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

        self.scrollArea = QScrollArea(SydTableWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 988, 69))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.layout_col_buttons = QHBoxLayout()
        self.layout_col_buttons.setObjectName(u"layout_col_buttons")
        self.button1 = QPushButton(self.scrollAreaWidgetContents)
        self.button1.setObjectName(u"button1")
        self.button1.setCheckable(False)

        self.layout_col_buttons.addWidget(self.button1)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.layout_col_buttons.addWidget(self.line)

        self.button2 = QPushButton(self.scrollAreaWidgetContents)
        self.button2.setObjectName(u"button2")
        font = QFont()
        font.setItalic(False)
        font.setStrikeOut(True)
        self.button2.setFont(font)
        self.button2.setCheckable(False)

        self.layout_col_buttons.addWidget(self.button2)

        self.button3 = QPushButton(self.scrollAreaWidgetContents)
        self.button3.setObjectName(u"button3")
        self.button3.setCheckable(False)
        self.button3.setFlat(True)

        self.layout_col_buttons.addWidget(self.button3)


        self.gridLayout.addLayout(self.layout_col_buttons, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.table_view = QTableView(SydTableWidget)
        self.table_view.setObjectName(u"table_view")

        self.verticalLayout.addWidget(self.table_view)


        self.retranslateUi(SydTableWidget)

        self.button2.setDefault(True)


        QMetaObject.connectSlotsByName(SydTableWidget)
    # setupUi

    def retranslateUi(self, SydTableWidget):
        SydTableWidget.setWindowTitle(QCoreApplication.translate("SydTableWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("SydTableWidget", u"Filter :", None))
        self.button1.setText(QCoreApplication.translate("SydTableWidget", u"dataset_name", None))
        self.button2.setText(QCoreApplication.translate("SydTableWidget", u"dataset_name", None))
        self.button3.setText(QCoreApplication.translate("SydTableWidget", u"dataset_name", None))
    # retranslateUi

