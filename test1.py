#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import syd
from PySide2.QtWidgets import QApplication
from ui import SydMainWindow

def main():
    app = QApplication(sys.argv)

    f = 'lu.db'
    db = syd.open_db(f)

    m = SydMainWindow()
    m.set_database(db)
    m.slot_on_change_table('Patient')
    m.show()
    app.exec_()


if __name__ == '__main__':
    main()