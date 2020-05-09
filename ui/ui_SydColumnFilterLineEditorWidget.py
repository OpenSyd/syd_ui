# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SydColumnFilterLineEditorWidget.ui'
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


class Ui_SydColumnFilterLineEditorWidget(object):
    def setupUi(self, SydColumnFilterLineEditorWidget):
        if not SydColumnFilterLineEditorWidget.objectName():
            SydColumnFilterLineEditorWidget.setObjectName(u"SydColumnFilterLineEditorWidget")
        SydColumnFilterLineEditorWidget.resize(133, 20)
        self.gridLayout = QGridLayout(SydColumnFilterLineEditorWidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line_edit = QLineEdit(SydColumnFilterLineEditorWidget)
        self.line_edit.setObjectName(u"line_edit")
        self.line_edit.setFrame(False)
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.line_edit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.line_edit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.line_edit, 0, 0, 1, 1)


        self.retranslateUi(SydColumnFilterLineEditorWidget)

        QMetaObject.connectSlotsByName(SydColumnFilterLineEditorWidget)
    # setupUi

    def retranslateUi(self, SydColumnFilterLineEditorWidget):
        SydColumnFilterLineEditorWidget.setWindowTitle(QCoreApplication.translate("SydColumnFilterLineEditorWidget", u"Form", None))
        self.line_edit.setPlaceholderText(QCoreApplication.translate("SydColumnFilterLineEditorWidget", u"Filter", None))
    # retranslateUi

