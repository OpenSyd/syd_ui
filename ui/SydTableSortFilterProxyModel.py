import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, Signal, QSortFilterProxyModel


class SydTableSortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self):
        super(SydTableSortFilterProxyModel, self).__init__()

    def filterAcceptsRow(self, source_row, source_parent):
        return True
