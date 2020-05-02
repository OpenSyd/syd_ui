from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from .SydColumnFilterHeader import SydColumnFilterHeader
from .SydTableModel import SydTableModel
from .SydTableSortFilterProxyModel import SydTableSortFilterProxyModel
from .ui_SydTableWidget import Ui_SydTableWidget


class SydTableWidget(QtWidgets.QWidget, Ui_SydTableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # internal members
        self._db = None
        self._data = None
        self._model = None
        self._filter_proxy_model = None
        self._header = None

    def set_data(self, db, data):
        self._db = db
        self._data = data

        # define and set the model
        self._model = SydTableModel(data)
        # self.table_view.setModel(self._model)

        # define own header (with column filter)
        self._header = SydColumnFilterHeader(self.table_view)
        ncol = self._model.columnCount(0)
        self.table_view.setHorizontalHeader(self._header)
        self._header.filterActivated.connect(self.handleFilterActivated)

        # define and set the filter/sort proxy
        self._filter_proxy_model = SydTableSortFilterProxyModel(self._header)
        self._filter_proxy_model.setSourceModel(self._model)
        self._filter_proxy_model.setSortLocaleAware(True)
        self._filter_proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.table_view.setModel(self._filter_proxy_model)

        # set it
        self._header.setFilterBoxes(ncol, self._filter_proxy_model)

    def handleFilterActivated(self):
        print('here')

