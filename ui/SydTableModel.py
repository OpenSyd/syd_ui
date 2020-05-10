from PySide2 import QtCore
from PySide2.QtCore import Qt, Signal
import syd
import copy
from datetime import datetime

class SydTableModel(QtCore.QAbstractTableModel):
    players_changed = Signal()

    def __init__(self, db, table, data):
        super(SydTableModel, self).__init__()

        # internal members
        self._db = db
        self._table = table
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
            # what if date ?ZZ
            if type(v) is int:
                return v
            return str(v)
        if role == Qt.EditRole:
            table = self._db[self._table]
            # update first in case something changed
            element = syd.find_one(table, id=element['id'])
            v = element[h]
            if v is None:
                return ''
            # what if date -> FIXME later with delegate
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
        col = index.column()
        if col == 0: # first is 'id', is not editable # FIXME do a list
            return original_flags
        return original_flags | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    # noinspection PyMethodOverriding
    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role != QtCore.Qt.EditRole:
             return False
        row = index.row()
        col = index.column()
        cname = self._headers[col]
        table = self._db[self._table]
        # update first
        element = self._data[row]
        #print('before update', element)
        #element = syd.find_one(table, id=element['id'])
        #print('after update', element)
        previous = copy.deepcopy(element)
        # special case for some type
        if isinstance(element[cname], datetime):
            element[cname] = syd.str_to_date(value)
        else:
            element[cname] = value
        # update the db
        try:
            syd.update_one(table, element)
            #return True
        except:
            # FIXME signal to warn user (status)
            print('Cannot update ERROR')
            self._data[index.row()] = previous
        return False

    # noinspection PyMethodOverriding
    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._headers[section]
        return None
