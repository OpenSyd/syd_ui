# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SydColumnFilterLineEditorWidget.ui',
# licensing of 'ui/SydColumnFilterLineEditorWidget.ui' applies.
#
# Created: Sat May  9 13:39:11 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SydColumnFilterLineEditorWidget(object):
    def setupUi(self, SydColumnFilterLineEditorWidget):
        SydColumnFilterLineEditorWidget.setObjectName("SydColumnFilterLineEditorWidget")
        SydColumnFilterLineEditorWidget.resize(133, 20)
        self.gridLayout = QtWidgets.QGridLayout(SydColumnFilterLineEditorWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_edit = QtWidgets.QLineEdit(SydColumnFilterLineEditorWidget)
        self.line_edit.setFrame(False)
        self.line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.line_edit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.line_edit.setClearButtonEnabled(True)
        self.line_edit.setObjectName("line_edit")
        self.gridLayout.addWidget(self.line_edit, 0, 0, 1, 1)

        self.retranslateUi(SydColumnFilterLineEditorWidget)
        QtCore.QMetaObject.connectSlotsByName(SydColumnFilterLineEditorWidget)

    def retranslateUi(self, SydColumnFilterLineEditorWidget):
        SydColumnFilterLineEditorWidget.setWindowTitle(QtWidgets.QApplication.translate("SydColumnFilterLineEditorWidget", "Form", None, -1))
        self.line_edit.setPlaceholderText(QtWidgets.QApplication.translate("SydColumnFilterLineEditorWidget", "Filter", None, -1))

