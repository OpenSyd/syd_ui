from PySide2 import QtCore
from PySide2.QtCore import Qt


class SydTableSortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self, header):
        super(SydTableSortFilterProxyModel, self).__init__()
        self._header = header
        self._filters = {}

    def filterAcceptsRow(self, source_row, source_parent):
        for key, regex in self._filters.items():
            ix = self.sourceModel().index(source_row, key, source_parent)
            if ix.isValid():
                text = self.sourceModel().data(ix, Qt.DisplayRole)
                if regex.indexIn(str(text)) == -1:
                    return False
        return True

    def setFilterByColumn(self, regex, column):
        self._filters[column] = regex
        self.invalidateFilter()