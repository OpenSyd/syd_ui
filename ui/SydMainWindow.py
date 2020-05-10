from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QAction, QProgressDialog
from .ui_SydMainWindow import Ui_SydMainWindow
from functools import partial
from ui import SydTableWidget
import syd


class SydMainWindow(QtWidgets.QMainWindow, Ui_SydMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._db = None
        # on OSX prefer to not be the native menu bar because focus issue
        self.menubar.setNativeMenuBar(False)


    def set_database(self, db):
        self._db = db
        # create tables menu
        for table in db.tables:
            a = QAction(self)
            a.setText(table)
            a.triggered.connect(partial(self.slot_on_change_table, table))
            self.menu_tables.addAction(a)


    def slot_on_change_table(self, table):
        self.statusbar.showMessage(f"Loading table {table}")
        db = self._db
        self._table = table
        elements = syd.find_all(db[table])
        # remove previous widget
        w = self.centralWidget()
        del w
        # setup table
        self._table_widget = SydTableWidget(self)
        self._table_widget.set_data(db, table, elements)
        self.setCentralWidget(self._table_widget)
        self._table_widget.button_reload.clicked.connect(self.slot_on_reload)


    def slot_on_reload(self):
        elements = syd.find_all(self._db[self._table])
        self._table_widget._model._data = elements
        self._table_widget._filter_proxy_model.invalidateFilter()
        self._table_widget._model.layoutChanged.emit()