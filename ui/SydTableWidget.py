
from PySide2 import QtWidgets
from PySide2.QtCore import Slot, Qt, QItemSelectionModel
from .ui_SydTableWidget import Ui_SydTableWidget
from .DicomSeriesTableModel import DicomSeriesTableModel
import syd

# center column
class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


class SydTableWidget(QtWidgets.QWidget, Ui_SydTableWidget):

    def __init__(self, parent=None):
        """
        Constructor
        """
        super().__init__(parent)
        self.setupUi(self)
        self._db = None
        self._model = None
        self.table_view.setAlternatingRowColors(True)
        self.table_view.setSortingEnabled(True)


    def set_db(self, db):
        self._db = db
        img = syd.find(db['DicomSeries'])

        self._model = DicomSeriesTableModel(img)
        self.table_view.setModel(self._model)

        delegate = AlignDelegate(self.table_view)
        for i in range(0,len(self._model.col_names)):
            self.table_view.setItemDelegateForColumn(i, delegate)
        self.table_view.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
