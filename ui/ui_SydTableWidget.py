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
        SydTableWidget.resize(1068, 548)
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

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(SydTableWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QSize(16777215, 32))
        self.scrollArea.setFrameShape(QFrame.Box)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContent = QWidget()
        self.scrollAreaContent.setObjectName(u"scrollAreaContent")
        self.scrollAreaContent.setGeometry(QRect(0, 0, 1046, 28))
        self.layout_col_buttons = QHBoxLayout(self.scrollAreaContent)
        self.layout_col_buttons.setSpacing(0)
        self.layout_col_buttons.setObjectName(u"layout_col_buttons")
        self.layout_col_buttons.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.layout_col_buttons.setContentsMargins(0, 0, 0, 0)
        self.button1 = QPushButton(self.scrollAreaContent)
        self.button1.setObjectName(u"button1")
        self.button1.setCheckable(False)

        self.layout_col_buttons.addWidget(self.button1)

        self.button2 = QPushButton(self.scrollAreaContent)
        self.button2.setObjectName(u"button2")
        font = QFont()
        font.setItalic(False)
        font.setStrikeOut(True)
        self.button2.setFont(font)
        self.button2.setCheckable(False)

        self.layout_col_buttons.addWidget(self.button2)

        self.button3 = QPushButton(self.scrollAreaContent)
        self.button3.setObjectName(u"button3")
        self.button3.setCheckable(False)
        self.button3.setFlat(True)

        self.layout_col_buttons.addWidget(self.button3)

        self.horizontalSpacer_2 = QSpacerItem(878, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_col_buttons.addItem(self.horizontalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaContent)

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

