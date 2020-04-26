import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, Signal
import syd

class DicomSeriesTableModel(QtCore.QAbstractTableModel):

    players_changed = Signal()

    def __init__(self, dicom_series):
        super(DicomSeriesTableModel, self).__init__()
        self._dicom_series = dicom_series
        self.headers=[]
        for h in dicom_series[0]:
            self.headers.append(h)
            # remove some header such as table_name
            # check all elements
        self.col_names = []
        self.col_names.extend(range(0,len(self.headers)))
        idx = 0
        for h in self.headers:
            self.col_names[idx] = h
            idx = idx + 1
            # remove some header such as table_name
            # check all elements

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            dicom = self._dicom_series[index.row()]
            c = index.column()
            h = self.col_names[c]
            v = dicom[h]
            return str(v)


    def rowCount(self, index):
        # The length of the outer list.
        return len(self._dicom_series)


    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.headers)


    def flags(self, index):
        original_flags = super(DicomSeriesTableModel, self).flags(index)
        #if index.column()>1:
        return original_flags
        #return original_flags | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


    def setData(self, index, value, role):
        #if not index.isValid():
        #    return False
        #if role != QtCore.Qt.EditRole:
        #     return False
        # row = index.row()
        # if row < 0 or row >= len(self._players):
        #     return False
        # column = index.column()
        # if column < 0 or column >= 2:
        #     return False
        # if column == 0:
        #     self._players[row].set_name(0, value)
        #     self.dataChanged.emit(index, index)
        #     return True
        # if column == 1:
        #     self._players[row].set_name(1, value)
        #     self.dataChanged.emit(index, index)
        #     return True
        return False

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.headers[section]
        return None

