from PySide2 import QtWidgets
from PySide2.QtCore import Qt, Signal, QRegExp
from .SydColumnFilterLineEditorWidget import SydColumnFilterLineEditorWidget


class SydColumnFilterHeader(QtWidgets.QHeaderView):

    filterActivated = Signal()

    def __init__(self, parent=None):
        super(SydColumnFilterHeader, self).__init__(Qt.Horizontal, parent)
        self.setSectionsClickable(True)
        self._editors = []
        self._padding = 2
        self._editor_height = 21
        self.sectionResized.connect(self.adjustPositions)
        parent.horizontalScrollBar().valueChanged.connect(self.adjustPositions)

    def setFilterBoxes(self, count, proxy):
        while self._editors:
            editor = self._editors.pop()
            editor.deleteLater()
        for index in range(count):
            editor = SydColumnFilterLineEditorWidget(self.parent())
            editor.line_edit.textChanged.connect(lambda text, col=index:
                                   proxy.setFilterByColumn(QRegExp(text,
                                                                   Qt.CaseInsensitive,
                                                                   QRegExp.FixedString),
                                                           col))
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
