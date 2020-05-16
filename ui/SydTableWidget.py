from PySide2 import QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QPushButton, QMenu, QAction
from PySide2.QtWidgets import QSizePolicy, QSpacerItem

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
        self._table = None
        self._model = None
        self._filter_proxy_model = None
        self._header = None
        self._toggle_width_menus = []

        # initial UI
        self.scrollArea.setVisible(False)

    def set_data(self, db, table, data):
        self._db = db
        self._data = data
        self._table = table

        # define and set the model
        self._model = SydTableModel(db, table, data)

        # define own header (with column filter)
        self._header = SydColumnFilterHeader(self.table_view)
        ncol = self._model.columnCount(0)
        self.table_view.setHorizontalHeader(self._header)

        # define and set the filter/sort proxy
        self._filter_proxy_model = SydTableSortFilterProxyModel(self._header)
        self._filter_proxy_model.setSourceModel(self._model)
        self._filter_proxy_model.setSortLocaleAware(True)
        self._filter_proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.table_view.setModel(self._filter_proxy_model)

        # set the columns filters
        self._header.set_filter_editors(ncol, self._filter_proxy_model)

        # setup the context menu
        self._header.setContextMenuPolicy(Qt.CustomContextMenu)
        self._header.customContextMenuRequested.connect(self.slot_on_column_header_popup)
        self._header.filterActivated.connect(self.slot_on_col_filter_changed)

        # remove previous col buttons
        c = self.layout_col_buttons.takeAt(0)
        while c and c.widget():
            c.widget().setParent(None)
            del c
            c = self.layout_col_buttons.takeAt(0)

        # create new col buttons
        def create_lambda(icol):
            return lambda: self.slot_on_col_button_clicked(icol)

        self.col_buttons = []
        for i in range(0, ncol):
            s = self._model._headers[i]
            b = QPushButton(s)  # , parent=self.layout_col_buttons)
            b.clicked.connect(create_lambda(i))
            b.setFlat(True)
            b.setVisible(False)
            self.layout_col_buttons.addWidget(b)
            self.col_buttons.append(b)
        h = QSpacerItem(878, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout_col_buttons.addItem(h)

        # create menu col width
        for i in range(0, ncol):
            b = QAction(self)
            b.setText('Toggle adjust width')
            b.setCheckable(True)
            b.setChecked(False)
            self._toggle_width_menus.append(b)
            # special case for first column ('id')
            if i == 0:
                b.setChecked(True)
                self.slot_on_auto_width_column(i)

        # make the area invisible first
        self.scrollArea.setVisible(False)

        # initial nb of elements
        self.slot_on_col_filter_changed()

        # double click header
        self.table_view.horizontalHeader().sectionDoubleClicked. \
            connect(self.slot_on_toggle_auto_width_column)

        # global filter
        self.edit_filter.textChanged.connect(self.slot_on_filter_changed)
        self.edit_filter.setClearButtonEnabled(True)

        # allow sorting
        self.table_view.setSortingEnabled(True)
        self._filter_proxy_model.sort(0, Qt.AscendingOrder)
        self._filter_proxy_model.invalidateFilter()
        self._header.updateGeometries()

    def slot_on_column_header_popup(self, pos):
        idx = self.table_view.horizontalHeader().logicalIndexAt(pos)
        menu = QMenu(self.table_view)
        a = QAction(self)
        name = self._model._col_names[idx]
        a.setText(f'Hide {name}')
        a.triggered.connect(lambda col_name=idx:
                            self.slot_on_hide_column(idx))
        b = self._toggle_width_menus[idx]
        b.triggered.connect(lambda col_name=idx:
                            self.slot_on_auto_width_column(idx))
        menu.addAction(a)
        menu.addAction(b)
        menu.exec_(self.table_view.mapToGlobal(pos))

    def slot_on_hide_column(self, idx):
        # hide the column
        self.table_view.setColumnHidden(idx, True)
        # show the button
        self.scrollArea.setVisible(True)
        self.col_buttons[idx].setVisible(True)
        self._header.updateGeometries()

    def slot_on_col_button_clicked(self, idx):
        # show the column
        self.table_view.setColumnHidden(idx, False)
        # hide the button
        self.col_buttons[idx].setVisible(False)
        for b in self.col_buttons:
            if b.isVisible():
                return
        self.scrollArea.setVisible(False)
        self._header.updateGeometries()

    def slot_on_toggle_auto_width_column(self, idx):
        b = self._toggle_width_menus[idx]
        b.setChecked(not b.isChecked())
        self.slot_on_auto_width_column(idx)

    def slot_on_auto_width_column(self, idx):
        b = self._toggle_width_menus[idx]
        if b.isChecked():
            self._header.setSectionResizeMode(idx, QtWidgets.QHeaderView.ResizeToContents)
        else:
            self._header.setSectionResizeMode(idx, QtWidgets.QHeaderView.Interactive)
        self._header.updateGeometries()

    def slot_on_col_filter_changed(self):
        n = self._filter_proxy_model.rowCount()
        t = self._model.rowCount(None)
        self.label_tablename.setText(f'{self._table}')
        self.label_status.setText(f'{n}/{t}')

    def slot_on_filter_changed(self):
        f = self.edit_filter
        self._filter_proxy_model.set_global_filter(f.text())
