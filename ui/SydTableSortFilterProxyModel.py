import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, Signal, QSortFilterProxyModel


class SydTableSortFilterProxyModel(QtCore.QSortFilterProxyModel):

    def __init__(self):
        super(SydTableSortFilterProxyModel, self).__init__()

    def filterAcceptsRow(self, source_row, source_parent):
        #print('filter', source_row, source_parent, self.filterRegExp())
        regex = self.filterRegExp()
        #print('pattern', regex.pattern())
        p = regex.pattern()
        for key in range(0,1):
            #print('key',key)
            ix = self.sourceModel().index(source_row, key, source_parent)
            #print('ix',ix)
            if ix.isValid():
                text = self.sourceModel().data(ix, Qt.DisplayRole)
                #print('text',text)
                if not p in str(text):
                    #print('false')
                    return False
                #print('True')
            else:
                print('invalid')
                #return True
        return True