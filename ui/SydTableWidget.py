from PySide2 import QtWidgets
from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QPushButton, QMenu, QAction
from PySide2.QtWidgets import QSizePolicy, QSpacerItem, QTableView

from .SydColumnFilterHeader import SydColumnFilterHeader
from .SydTableModel import SydTableModel
from .SydTableSortFilterProxyModel import SydTableSortFilterProxyModel
from .ui_SydTableWidget import Ui_SydTableWidget
from .SydCTWindow import SydCTWindow
import syd
import os


class SydTableWidget(QtWidgets.QWidget, Ui_SydTableWidget):
    table_reloaded = Signal()

    def __init__(self, filename, table_name, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # internal members
        self._filename = filename
        self._table_name = table_name
        self._db = None
        self._data = None
        self._model = None
        self._filter_proxy_model = None
        self._header = None
        self._toggle_width_menus = []
        self.button_reload.clicked.connect(self.slot_on_reload)
        self.button_view.hide()
        self.button_view.clicked.connect(self.slot_on_view)

        # initial UI
        # self.setAutoFillBackground(True)
        self.scrollArea.setVisible(False)
        self.button_view.setEnabled(False)

        # pop-up window
        self.w = None

    def table_name(self):
        return self._table_name

    def model(self):
        return self._model

    def set_data(self, data):
        self._data = data
        db = self._db
        table_name = self._table_name

        # define and set the model
        self._model = SydTableModel(self._filename, db, table_name, data)

        # remove previous widget
        self.table_view.setParent(None)
        del self.table_view

        # create new one
        self.table_view = QTableView(self)
        self.verticalLayout.addWidget(self.table_view)

        # define own header (with column filter)
        self._header = SydColumnFilterHeader(self.table_view)
        ncol = self._model.columnCount(0)

        # define and set the filter/sort proxy
        self._filter_proxy_model = SydTableSortFilterProxyModel(self._header)
        self._filter_proxy_model.setSourceModel(self._model)
        self._filter_proxy_model.setSortLocaleAware(True)
        self._filter_proxy_model.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.table_view.setModel(self._filter_proxy_model)

        # selection model for the button_view
        self.table_view.setSelectionBehavior(QTableView.SelectRows)
        selection = self.table_view.selectionModel()
        selection.selectionChanged.connect(self.on_selection_change)

        # set the columns filters
        self._header.set_filter_editors(ncol, self._filter_proxy_model)

        # setup the context menu
        self._header.setContextMenuPolicy(Qt.CustomContextMenu)
        self._header.customContextMenuRequested.connect(self.slot_on_column_header_popup)
        self._header.filterActivated.connect(self.slot_on_col_filter_changed)

        self.table_view.setHorizontalHeader(self._header)

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
        # self.scrollArea.setAutoFillBackground(True)
        # self.table_view.setAutoFillBackground(True)
        self.table_view.setAlternatingRowColors(True)

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
        self.label_tablename.setText(f'{self._table_name}')
        self.label_status.setText(f'{n}/{t}')
        if self._table_name == 'Image' or self._table_name == 'DicomSeries':
            self.button_view.show()
        elif self._table_name == "DicomSeries_default" or self._table_name == "Image_default":
            self.button_view.show()

    def slot_on_filter_changed(self):
        n = self._filter_proxy_model.rowCount()
        t = self._model.rowCount(None)
        self.label_status.setText(f'{n}/{t}')
        f = self.edit_filter
        self._filter_proxy_model.set_global_filter(f.text())

    def slot_on_reload(self):
        # later -> keep filters if the columns are identical.
        # not clear why I need to reopen the db here
        # (not needed for tables, needed for view)
        self._db = syd.open_db(self._filename)
        t = self._db.load_table(self._table_name)
        elements = syd.find_all(t)
        self.set_data(elements)
        # indicate that the table has been reloaded
        self.table_reloaded.emit()
        n = self._filter_proxy_model.rowCount()
        t = self._model.rowCount(None)
        self.label_status.setText(f'{n}/{t}')
        self.button_view.setText("view in vv")
        self.button_view.setEnabled(False)

    def slot_on_view(self):
        data = []
        path = []
        selectedRows = self.table_view.selectedIndexes()
        modelRows = []
        for selectedRow in selectedRows:
          modelRows.append(self._filter_proxy_model.mapToSource(selectedRow).row())
        rows = set(modelRows)
        for row in rows:
            data.append(self._data[row])
        self.w = SydCTWindow(data, self._filename, self._table_name)
        self.w.button_ct_on.setEnabled(False)
        db = syd.open_db(self._filename)
        for d in data:
            if self._table_name == 'Image_default':
                db = syd.open_db(self._filename)
                d = syd.find_one(db['Image'], id=d['id'])
            if self._table_name == 'DicomSeries' or self._table_name == 'DicomSeries_default':
                e = self.w.get_ct_path_from_dicomSerie(db, d["id"])
            elif self._table_name == 'Image' or self._table_name == 'Image_default':
                e = self.w.get_ct_path_from_image(db, d)
            if e is not None and len(rows) == 1 and d['modality'] != 'CT':
                self.w.button_ct_on.setEnabled(True)
                self.w.show()
            else:
                if self._table_name == 'DicomSeries' or self._table_name == 'DicomSeries_default':
                    db = syd.open_db(self._filename)
                    dicom_file = syd.find_one(db['DicomFile'], dicom_series_id=d['id'])
                    file = syd.find_one(db['File'], id=dicom_file['file_id'])
                    tmp = db.absolute_data_folder + '/' + file['folder'] + '/' + file['filename']
                    path.append(tmp)
                elif self._table_name == 'Image' or self._table_name == 'Image_default':
                    db = syd.open_db(self._filename)
                    file = syd.find_one(db['File'], id=d['file_mhd_id'])
                    path.append(db.absolute_data_folder + '/' + file['folder'] + '/' + file['filename'])
                else:
                    print('La table séléctionnée ne correspond pas')
        if path != []:
            path = ' '.join(path)
            cmd = f'vv {path}'
            os.system(cmd)
        else:
            print('Path to image has no corresponding file')

    def on_selection_change(self):
        rows = set(index.row() for index in self.table_view.selectedIndexes())
        if len(rows) == 0:
            self.button_view.setEnabled(False)
            self.button_view.setText("view in vv")
        else:
            t = self._model.rowCount(None)
            self.button_view.setText(f"view in vv {len(rows)}/{t}")
            self.button_view.setEnabled(True)
