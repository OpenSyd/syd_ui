from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Qt, QItemSelectionModel, QDateTime
# from .ui_SydTableView import Ui_SydTableView
from .SydTableModel import SydTableModel
from PySide2.QtWidgets import QPushButton, QFrame
from PySide2.QtWidgets import QDateTimeEdit, QLabel, QMenu, QAction, QLineEdit
from PySide2.QtGui import QFont
from .SydTableSortFilterProxyModel import SydTableSortFilterProxyModel

import syd


class SydTableView(QtWidgets.QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
