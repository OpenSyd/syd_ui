#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import syd
from PySide2.QtWidgets import QApplication
from ui import SydTableWidget

app = QApplication(sys.argv)

f = 'lu.db'
db = syd.open_db(f)
img = syd.find(db['DicomSeries'])

m = SydTableWidget()
m.set_data(db, img)
m.show()

app.exec_()
