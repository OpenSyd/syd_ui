from PySide2 import QtCore
from PySide2.QtCore import Qt, QRegExp


class SydTableSortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self, header):
        super(SydTableSortFilterProxyModel, self).__init__()
        self._header = header
        self._filters = {}
        self._global_filter = \
            QRegExp('', Qt.CaseInsensitive, QRegExp.FixedString)

    def filterAcceptsRow(self, source_row, source_parent):
        # column filters
        for key, regex in self._filters.items():
            ix = self.sourceModel().index(source_row, key, source_parent)
            if ix.isValid():
                text = self.sourceModel().data(ix, Qt.DisplayRole)
                if regex.indexIn(str(text)) == -1:
                    return False
        # global filter
        for key in range(len(self._header._editors)):
            ix = self.sourceModel().index(source_row, key, source_parent)
            text = self.sourceModel().data(ix, Qt.DisplayRole)
            if self._global_filter.indexIn(str(text)) != -1:
                return True
        return False

    def set_filter_by_column(self, regex, column):
        self._filters[column] = regex
        self.invalidateFilter()

    def set_global_filter(self, text):
        r = QRegExp(text,
                    Qt.CaseInsensitive,
                    QRegExp.FixedString)
        self._global_filter = r
        self.invalidateFilter()
