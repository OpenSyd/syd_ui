from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Qt, QItemSelectionModel, QDateTime
from .ui_SydTableWidget import Ui_SydTableWidget
from .SydTableModel import SydTableModel
from PySide2.QtWidgets import QPushButton, QFrame
from PySide2.QtWidgets import QDateTimeEdit, QLabel, QMenu, QAction, QLineEdit
from PySide2.QtGui import QFont
from .SydTableSortFilterProxyModel import SydTableSortFilterProxyModel
from .SydColumnFilterHeader import SydColumnFilterHeader

class SydTableWidget(QtWidgets.QWidget, Ui_SydTableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # internal members
        self._db = None
        self._data = None
        self._model = None
        self._filter_proxy_model = None

    def set_data(self, db, data):
        self._db = db
        self._data = data

        # define and set the model
        self._model = SydTableModel(data)
        # self.table_view.setModel(self._model)

        # define and set the filter/sort proxy
        self._filter_proxy_model = SydTableSortFilterProxyModel()
        self._filter_proxy_model.setSourceModel(self._model)
        self._filter_proxy_model.setSortLocaleAware(True)
        self._filter_proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.table_view.setModel(self._filter_proxy_model)

        # define own header (with column filter)
        header = SydColumnFilterHeader(self.table_view)
        ncol = self._model.columnCount(0)
        header.setFilterBoxes(ncol)
        self.table_view.setHorizontalHeader(header)

