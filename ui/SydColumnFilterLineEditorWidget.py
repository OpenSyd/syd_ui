from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Qt, QItemSelectionModel, QDateTime
from .ui_SydColumnFilterLineEditorWidget import Ui_SydColumnFilterLineEditorWidget
from .SydTableModel import SydTableModel
from PySide2.QtWidgets import QPushButton, QFrame
from PySide2.QtWidgets import QDateTimeEdit, QLabel, QMenu, QAction, QLineEdit
from PySide2.QtGui import QFont
from .SydTableSortFilterProxyModel import SydTableSortFilterProxyModel

class SydColumnFilterLineEditorWidget(QtWidgets.QWidget,
                                      Ui_SydColumnFilterLineEditorWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.line_edit.setClearButtonEnabled(True)
        self.line_edit.setPlaceholderText('Filter')
