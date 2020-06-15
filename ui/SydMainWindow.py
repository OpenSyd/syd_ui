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
        self._table_name = None
        self._filename = None
        # on OSX prefer to not be the native menu bar because focus issue
        self.menubar.setNativeMenuBar(False)

    def set_database(self, filename):
        db = syd.open_db(filename)
        self._db = db
        self._filename = filename
        self.setWindowTitle(filename)
        self.setup_table_menus()

    def setup_table_menus(self):
        db = self._db
        self.menu_tables.clear()
        self.menu_views.clear()
        # create tables menu
        for table in db.tables:
            a = QAction(self)
            a.setText(table)
            a.triggered.connect(partial(self.slot_on_load_new_table, table))
            self.menu_tables.addAction(a)

        # create views menu
        views = syd.get_view_names(db)
        for v in views:
            a = QAction(self)
            a.setText(v)
            a.triggered.connect(partial(self.slot_on_load_new_table, v))
            self.menu_views.addAction(a)

    def slot_on_load_new_table(self, table_name):
        self._table_name = table_name

        # table already loaded in a tab ?
        for i in range(self.tab_widget.count()):
            w = self.tab_widget.widget(i)
            if w.table_name() == table_name:
                w.slot_on_reload()
                self.tab_widget.setCurrentIndex(i)
                return

        # new tab
        self.statusbar.showMessage(f"{table_name} table loaded")
        w = SydTableWidget(self._filename, table_name, self)
        #w.setAutoFillBackground(True)
        self.tab_widget.addTab(w, f"{table_name}")
        idx = self.tab_widget.indexOf(w)
        #self.tab_widget.setAutoFillBackground(True)
        # w.button_reload.clicked.connect(partial(self.slot_on_reload, idx))
        # self._table_widget.table_should_reload.connect(self.slot_on_reload_table())
        w.slot_on_reload()
        w.table_reloaded.connect(partial(self.slot_on_table_reloaded, idx))
        self.tab_widget.setCurrentIndex(idx)
        w.model().table_should_reload.connect(self.slot_on_table_should_reload)

    def slot_on_table_reloaded(self, idx):
        w = self.tab_widget.widget(idx)
        table_name = w.table_name()
        self.statusbar.showMessage(f"{table_name} table reloaded")
        # re-setup the menus, because views may have changed
        self.setup_table_menus()

    def slot_on_table_should_reload(self, source_table, table_name):
        # reload the given table_name
        # reload all views except the source
        for i in range(self.tab_widget.count()):
            w = self.tab_widget.widget(i)
            n = w.table_name()
            if n == table_name and n != source_table:
                w.slot_on_reload()
            if '_' in n and n != source_table:
                w.slot_on_reload()
