# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SydTableWidget.ui',
# licensing of 'ui/SydTableWidget.ui' applies.
#
# Created: Sat May  9 13:39:11 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SydTableWidget(object):
    def setupUi(self, SydTableWidget):
        SydTableWidget.setObjectName("SydTableWidget")
        SydTableWidget.resize(1068, 548)
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
        self.label_status = QtWidgets.QLabel(SydTableWidget)
        self.label_status.setObjectName("label_status")
        self.horizontalLayout.addWidget(self.label_status)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(SydTableWidget)
        self.scrollArea.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 32))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContent = QtWidgets.QWidget()
        self.scrollAreaContent.setGeometry(QtCore.QRect(0, 0, 1046, 28))
        self.scrollAreaContent.setObjectName("scrollAreaContent")
        self.layout_col_buttons = QtWidgets.QHBoxLayout(self.scrollAreaContent)
        self.layout_col_buttons.setSpacing(0)
        self.layout_col_buttons.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_col_buttons.setContentsMargins(0, 0, 0, 0)
        self.layout_col_buttons.setObjectName("layout_col_buttons")
        self.button1 = QtWidgets.QPushButton(self.scrollAreaContent)
        self.button1.setCheckable(False)
        self.button1.setObjectName("button1")
        self.layout_col_buttons.addWidget(self.button1)
        self.button2 = QtWidgets.QPushButton(self.scrollAreaContent)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(True)
        self.button2.setFont(font)
        self.button2.setCheckable(False)
        self.button2.setDefault(True)
        self.button2.setObjectName("button2")
        self.layout_col_buttons.addWidget(self.button2)
        self.button3 = QtWidgets.QPushButton(self.scrollAreaContent)
        self.button3.setCheckable(False)
        self.button3.setFlat(True)
        self.button3.setObjectName("button3")
        self.layout_col_buttons.addWidget(self.button3)
        spacerItem1 = QtWidgets.QSpacerItem(878, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_col_buttons.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaContent)
        self.verticalLayout.addWidget(self.scrollArea)
        self.table_view = QtWidgets.QTableView(SydTableWidget)
        self.table_view.setObjectName("table_view")
        self.verticalLayout.addWidget(self.table_view)

        self.retranslateUi(SydTableWidget)
        QtCore.QMetaObject.connectSlotsByName(SydTableWidget)

    def retranslateUi(self, SydTableWidget):
        SydTableWidget.setWindowTitle(QtWidgets.QApplication.translate("SydTableWidget", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("SydTableWidget", "Filter :", None, -1))
        self.label_status.setText(QtWidgets.QApplication.translate("SydTableWidget", "TextLabel", None, -1))
        self.button1.setText(QtWidgets.QApplication.translate("SydTableWidget", "dataset_name", None, -1))
        self.button2.setText(QtWidgets.QApplication.translate("SydTableWidget", "dataset_name", None, -1))
        self.button3.setText(QtWidgets.QApplication.translate("SydTableWidget", "dataset_name", None, -1))

