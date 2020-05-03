from PySide2 import QtCore
from PySide2.QtCore import Qt, Signal


class SydTableModel(QtCore.QAbstractTableModel):
    players_changed = Signal()

    def __init__(self, data):
        super(SydTableModel, self).__init__()

        # internal members
        self._data = data
        self._headers = []
        self._col_names = []

        # create headers
        for h in data[0]:
            self._headers.append(h)
            # remove some header such as table_name
            # check all elements
        self._col_names.extend(range(0, len(self._headers)))
        idx = 0
        for h in self._headers:
            self._col_names[idx] = h
            idx = idx + 1
            # remove some header such as table_name
            # check all elements

    # noinspection PyMethodOverriding
    def data(self, index, role):
        element = self._data[index.row()]
        c = index.column()
        h = self._col_names[c]
        v = element[h]
        if role == Qt.DisplayRole:
            if v is None:
                return ''
            # what if date ?
            if type(v) is int:
                return v
            return str(v)

    # noinspection PyMethodOverriding
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    # noinspection PyMethodOverriding
    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._headers)

    def flags(self, index):
        original_flags = super(SydTableModel, self).flags(index)
        # if index.column()>1:
        # return original_flags
        return original_flags | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    # noinspection PyMethodOverriding
    def setData(self, index, value, role):
        # if not index.isValid():
        #    return False
        # if role != QtCore.Qt.EditRole:
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

    # noinspection PyMethodOverriding
    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._headers[section]
        return None
