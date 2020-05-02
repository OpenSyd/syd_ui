
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Qt, QItemSelectionModel, QDateTime
from .ui_SydTableWidget import Ui_SydTableWidget
#from .DicomSeriesTableModel import DicomSeriesTableModel
from PySide2.QtWidgets import QPushButton, QFrame
from PySide2.QtWidgets import QDateTimeEdit, QLabel, QMenu, QAction, QLineEdit
from PySide2.QtGui import QFont
from .SydTableSortFilterProxyModel import SydTableSortFilterProxyModel
from .SydColumnFilterLineEditorWidget import SydColumnFilterLineEditorWidget

import syd

class SydColumnFilterHeader(QtWidgets.QHeaderView):
    def __init__(self, parent=None):
        super(SydColumnFilterHeader, self).__init__(Qt.Horizontal, parent)
        #self.button = QtWidgets.QPushButton('Button text', self)
        #print('iir')
        #self.setSortIndicatorShown(True)
        self.setSectionsClickable(True)
        self._editors = []
        self._padding = 2
        self._editor_height = 21
        self.sectionResized.connect(self.adjustPositions)
        parent.horizontalScrollBar().valueChanged.connect(self.adjustPositions)

    def setFilterBoxes(self, count):
        while self._editors:
            editor = self._editors.pop()
            editor.deleteLater()
        for index in range(count):
            editor = SydColumnFilterLineEditorWidget(self.parent())
            # editor.returnPressed.connect(self.filterActivated.emit)
            self._editors.append(editor)
        self.adjustPositions()

    def adjustPositions(self):
        for index, editor in enumerate(self._editors):
            # cannot really use editor height, because not always equal
            # height = editor.sizeHint().height()
            height = self._editor_height
            editor.move(
                self.sectionPosition(index) - self.offset() + 6,
                height + (self._padding // 2))
            editor.resize(self.sectionSize(index)-2, height)

    def sizeHint(self):
        size = super().sizeHint()
        if self._editors:
            height = self._editors[0].sizeHint().height()
            size.setHeight(size.height() + height + self._padding)
        return size

    def updateGeometries(self):
        if self._editors:
            height = self._editors[0].sizeHint().height()
            self.setViewportMargins(0, 0, 0, height + self._padding)
        else:
            self.setViewportMargins(0, 0, 0, 0)
        super().updateGeometries()
        self.adjustPositions()

