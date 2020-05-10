from PySide2 import QtWidgets

from .ui_SydColumnFilterLineEditorWidget import Ui_SydColumnFilterLineEditorWidget


class SydColumnFilterLineEditorWidget(QtWidgets.QWidget,
                                      Ui_SydColumnFilterLineEditorWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.line_edit.setClearButtonEnabled(True)
        self.line_edit.setPlaceholderText('Filter')

