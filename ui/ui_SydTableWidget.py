# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SydTableWidget.ui',
# licensing of 'ui/SydTableWidget.ui' applies.
#
# Created: Sat May  2 21:48:02 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SydTableWidget(object):
    def setupUi(self, SydTableWidget):
        SydTableWidget.setObjectName("SydTableWidget")
        SydTableWidget.resize(1008, 668)
        self.verticalLayout = QtWidgets.QVBoxLayout(SydTableWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SydTableWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.edit_filter = QtWidgets.QLineEdit(SydTableWidget)
        self.edit_filter.setMinimumSize(QtCore.QSize(200, 0))
        self.edit_filter.setMaximumSize(QtCore.QSize(200, 16777215))
        self.edit_filter.setObjectName("edit_filter")
        self.horizontalLayout.addWidget(self.edit_filter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(SydTableWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 988, 69))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.layout_col_buttons = QtWidgets.QHBoxLayout()
        self.layout_col_buttons.setObjectName("layout_col_buttons")
        self.button1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button1.setCheckable(False)
        self.button1.setObjectName("button1")
        self.layout_col_buttons.addWidget(self.button1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layout_col_buttons.addWidget(self.line)
        self.button2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(True)
        self.button2.setFont(font)
        self.button2.setCheckable(False)
        self.button2.setDefault(True)
        self.button2.setObjectName("button2")
        self.layout_col_buttons.addWidget(self.button2)
        self.button3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.button3.setCheckable(False)
        self.button3.setFlat(True)
        self.button3.setObjectName("button3")
        self.layout_col_buttons.addWidget(self.button3)
        self.gridLayout.addLayout(self.layout_col_buttons, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.table_view = QtWidgets.QTableView(SydTableWidget)
        self.table_view.setObjectName("table_view")
        self.verticalLayout.addWidget(self.table_view)

        self.retranslateUi(SydTableWidget)
        QtCore.QMetaObject.connectSlotsByName(SydTableWidget)

    def retranslateUi(self, SydTableWidget):
        SydTableWidget.setWindowTitle(QtWidgets.QApplication.translate("SydTableWidget", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("SydTableWidget", "Filter :", None, -1))
        self.button1.setText(QtWidgets.QApplication.translate("SydTableWidget", "dataset_name", None, -1))
        self.button2.setText(QtWidgets.QApplication.translate("SydTableWidget", "dataset_name", None, -1))
        self.button3.setText(QtWidgets.QApplication.translate("SydTableWidget", "dataset_name", None, -1))

