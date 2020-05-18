from PySide2 import QtCore
from PySide2.QtCore import Qt, Signal
import syd
import copy
from datetime import datetime


class SydTableModel(QtCore.QAbstractTableModel):

    table_should_reload = Signal(str, str)

    def __init__(self, filename, db, table, data):
        super(SydTableModel, self).__init__()

        # internal members
        self._filename = filename
        self._db = db
        self._table = table
        self._data = data
        self._headers = []
        self._col_names = []

        # create headers
        for h in db[table].columns:#data[0]:
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
            if type(v) is int or type(v) is float:
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
        if col == 0:  # first is 'id', is not editable # FIXME do a list
            return original_flags
        return original_flags | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    # noinspection PyMethodOverriding
    def setData(self, index, value, role):
        # return if no edit
        if not index.isValid():
            return False
        if role != QtCore.Qt.EditRole:
            return False

        # prepare information
        row = index.row()
        col = index.column()
        col_name = self._headers[col]
        table_name = self._table
        db = self._db

        # copy previous in case of error
        element = self._data[row]
        previous = copy.deepcopy(element)

        # determine if view or table
        # if it is a view, must get the real col and table
        real_col_name = col_name
        real_table_name = table_name
        real_element = element
        if table_name not in db.tables:
            view = syd.find_one(db['FormatView'], view_name=table_name)
            columns_format = syd.parse_columns_view_format(db, view.format)
            format = columns_format[col_name]
            if len(format.tables) > 0:
                real_table_name = format.tables[-1]
                rid = real_table_name.lower() + '_id'
            else:
                real_table_name = view.table_name
                rid = 'id'
            real_col_name = format.id
            e = syd.find_one(db[view.table_name], id=element.id)
            real_element = syd.find_one(self._db[real_table_name], id=e[rid])

        # special case for some type
        if isinstance(real_element[real_col_name], datetime):
            real_element[real_col_name] = syd.str_to_date(value)
        else:
            real_element[real_col_name] = value

        # update the db
        try:
            syd.update_one(db[real_table_name], real_element)
            # if this is a view, update view
            if real_table_name != table_name:
                self._data = syd.find_all(db[table_name])
            # other views/tables may be updated
            self.table_should_reload.emit(table_name, real_table_name)
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
