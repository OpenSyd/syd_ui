#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PySide2.QtWidgets import QApplication

from ui import SydMainWindow


def main():
    app = QApplication(sys.argv)
    f = 'lu.db'
    m = SydMainWindow()
    m.set_database(f)
    m.slot_on_change_table('Patient')
    m.show()
    app.exec_()


if __name__ == '__main__':
    main()
