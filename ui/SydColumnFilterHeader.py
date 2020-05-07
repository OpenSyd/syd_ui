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
        self._editors_idx = []
        self._proxy = None
        self.sectionResized.connect(self.adjustPositions)
        self.setSectionsMovable(True)
        parent.horizontalScrollBar().valueChanged.connect(self.adjustPositions)
        self.sectionMoved.connect(self.slot_on_section_moved)

    def set_filter_editors(self, count, proxy):
        self._proxy = proxy
        while self._editors:
            editor = self._editors.pop()
            editor.deleteLater()
        for index in range(count):
            editor = SydColumnFilterLineEditorWidget(self.parent())
            editor.line_edit.textChanged.connect(lambda text, col=index:
                                                 self.slot_on_filer_text_changed(text, col))
            self._editors.append(editor)
            self._editors_idx.append(index)
        self.adjustPositions()

    def adjustPositions(self):
        for vindex in range(len(self._editors)):
            idx = self.logicalIndex(vindex)  # because column may have move
            editor = self._editors[idx]
            # not clear which height to take.
            # height = editor.sizeHint().height()
            height = self._editor_height
            editor.move(
                self.sectionPosition(idx) - self.offset() + 6,
                height + (self._padding // 2))
            editor.resize(self.sectionSize(idx) - 2, height)
            # editor.line_edit.setPlaceholderText(f'{vindex} {idx}')

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

    def slot_on_section_moved(self):
        # other args: logicalIndex, oldVisualIndex, newVisualIndex
        self.adjustPositions()

    def slot_on_filer_text_changed(self, text, col):
        self._proxy.set_filter_by_column(QRegExp(text,
                                           Qt.CaseInsensitive,
                                           QRegExp.FixedString), col)
        self.filterActivated.emit()
