from PySide2 import QtWidgets


class SydTableView(QtWidgets.QTableView):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAlternatingRowColors(True)
        self.setSortingEnabled(True)
        self.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
