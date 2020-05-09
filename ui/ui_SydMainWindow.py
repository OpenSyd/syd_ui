# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/SydMainWindow.ui',
# licensing of 'ui/SydMainWindow.ui' applies.
#
# Created: Sat May  9 13:39:11 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SydMainWindow(object):
    def setupUi(self, SydMainWindow):
        SydMainWindow.setObjectName("SydMainWindow")
        SydMainWindow.resize(879, 621)
        self.central_widget = QtWidgets.QWidget(SydMainWindow)
        self.central_widget.setObjectName("central_widget")
        SydMainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_tables = QtWidgets.QMenu(self.menubar)
        self.menu_tables.setObjectName("menu_tables")
        SydMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SydMainWindow)
        self.statusbar.setObjectName("statusbar")
        SydMainWindow.setStatusBar(self.statusbar)
        self.actionPatient = QtWidgets.QAction(SydMainWindow)
        self.actionPatient.setObjectName("actionPatient")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_tables.menuAction())

        self.retranslateUi(SydMainWindow)
        QtCore.QMetaObject.connectSlotsByName(SydMainWindow)

    def retranslateUi(self, SydMainWindow):
        SydMainWindow.setWindowTitle(QtWidgets.QApplication.translate("SydMainWindow", "MainWindow", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("SydMainWindow", "File", None, -1))
        self.menu_tables.setTitle(QtWidgets.QApplication.translate("SydMainWindow", "Tables", None, -1))
        self.actionPatient.setText(QtWidgets.QApplication.translate("SydMainWindow", "Patient", None, -1))

