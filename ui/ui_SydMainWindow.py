# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SydMainWindow.ui'
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


class Ui_SydMainWindow(object):
    def setupUi(self, SydMainWindow):
        if not SydMainWindow.objectName():
            SydMainWindow.setObjectName(u"SydMainWindow")
        SydMainWindow.resize(936, 612)
        self.actionQuit = QAction(SydMainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.central_widget = QWidget(SydMainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.gridLayout = QGridLayout(self.central_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setObjectName(u"tab_widget")

        self.gridLayout.addWidget(self.tab_widget, 0, 0, 1, 1)

        SydMainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(SydMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 936, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menu_tables = QMenu(self.menubar)
        self.menu_tables.setObjectName(u"menu_tables")
        self.menu_views = QMenu(self.menubar)
        self.menu_views.setObjectName(u"menu_views")
        SydMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SydMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        SydMainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_tables.menuAction())
        self.menubar.addAction(self.menu_views.menuAction())
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(SydMainWindow)
        self.actionQuit.triggered.connect(SydMainWindow.close)

        self.tab_widget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(SydMainWindow)
    # setupUi

    def retranslateUi(self, SydMainWindow):
        SydMainWindow.setWindowTitle(QCoreApplication.translate("SydMainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("SydMainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("SydMainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("SydMainWindow", u"File", None))
        self.menu_tables.setTitle(QCoreApplication.translate("SydMainWindow", u"Tables", None))
        self.menu_views.setTitle(QCoreApplication.translate("SydMainWindow", u"Views", None))
    # retranslateUi

