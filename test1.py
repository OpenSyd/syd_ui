#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import syd
from PySide2.QtWidgets import QApplication
from syd_ui.ui import SydTableWidget

f = 'lu.db'
db = syd.open_db(f)

app = QApplication(sys.argv)
m = SydTableWidget()
m.set_db(db)

m.show()
app.exec_()
