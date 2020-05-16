from functools import partial

import syd
from PySide2 import QtWidgets
from PySide2.QtWidgets import QAction

from ui import SydTableWidget
from .ui_SydMainWindow import Ui_SydMainWindow


class SydMainWindow(QtWidgets.QMainWindow, Ui_SydMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._db = None
        self._table = None
        self._table_widget = None
        self._filename = None
        # on OSX prefer to not be the native menu bar because focus issue
        self.menubar.setNativeMenuBar(False)

    def set_database(self, filename):
        db = syd.open_db(filename)
        self._db = db
        self._filename = filename

        # create tables menu
        for table in db.tables:
            a = QAction(self)
            a.setText(table)
            a.triggered.connect(partial(self.slot_on_change_table, table))
            self.menu_tables.addAction(a)

        # create views menu
        views = syd.get_view_names(db)
        for v in views:
            a = QAction(self)
            a.setText(v)
            a.triggered.connect(partial(self.slot_on_change_table, v))
            self.menu_views.addAction(a)

    def slot_on_change_table(self, table):
        self.statusbar.showMessage(f"{table} table loaded")
        # not clear why I need to reopen the db here
        # (not needed for tables, needed for view)
        db = syd.open_db(self._filename)
        self._table = table
        t = db.load_table(table)
        print(t.columns)
        elements = syd.find_all(t)
        # remove previous widget
        w = self.centralWidget()
        del w
        # setup table
        self._table_widget = SydTableWidget(self)
        self._table_widget.set_data(db, table, elements)
        self.setCentralWidget(self._table_widget)
        self._table_widget.button_reload.clicked.connect(self.slot_on_reload)

    def slot_on_reload(self):
        # later -> keep filters if the columns are identical
        self.slot_on_change_table(self._table)
