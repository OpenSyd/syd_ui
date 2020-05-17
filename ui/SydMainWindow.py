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
        self.setup_table_menus()

    def setup_table_menus(self):
        db = self._db
        self.menu_tables.clear()
        self.menu_views.clear()
        # create tables menu
        for table in db.tables:
            a = QAction(self)
            a.setText(table)
            a.triggered.connect(partial(self.slot_on_load_table, table))
            self.menu_tables.addAction(a)

        # create views menu
        views = syd.get_view_names(db)
        for v in views:
            a = QAction(self)
            a.setText(v)
            a.triggered.connect(partial(self.slot_on_load_table, v))
            self.menu_views.addAction(a)

    def slot_on_load_table(self, table):
        self._table = table

        # table already loaded in a tab ?
        for i in range(self.tab_widget.count()):
            if self.tab_widget.widget(i)._table == table:
                self.slot_on_reload(i)
                self.tab_widget.setCurrentIndex(i)
                return

        # new tab
        self.statusbar.showMessage(f"{table} table loaded")
        self._table_widget = SydTableWidget(table, self)
        self.tab_widget.addTab(self._table_widget, f"{table}")
        idx = self.tab_widget.indexOf(self._table_widget)
        self._table_widget.button_reload.clicked.connect(partial(self.slot_on_reload, idx))
        self.slot_on_reload(idx)
        self.tab_widget.setCurrentIndex(idx)

    def slot_on_reload(self, tab_index):
        # later -> keep filters if the columns are identical.
        # not clear why I need to reopen the db here
        # (not needed for tables, needed for view)
        db = syd.open_db(self._filename)
        w = self.tab_widget.widget(tab_index)
        table = w._table
        t = db.load_table(table)
        elements = syd.find_all(t)
        w.set_data(db, table, elements)
        # re-setup the menus, because views may changed 
        self.setup_table_menus()

