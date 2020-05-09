#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform

def gen_ui(win, name):
    print(f'Generate UI {name}')
    if win:
        os.system('..\\venv\\Scripts\pyside2-uic.exe ui\\' + name + '.ui -o ui\\ui_' + name + '.py')
    else:
        os.system('pyside2-uic ui/' + name + '.ui -o ui/ui_' + name + '.py')

s = platform.platform()

w = False
if 'Windows' in  s:
    print('Platform is windows')
    w = True
else:
    print('Platform is not windows')

gen_ui(w, 'SydMainWindow')
gen_ui(w, 'SydTableWidget')
gen_ui(w, 'SydColumnFilterLineEditorWidget')

#print('Generate RC')
#if w:
#    os.system("..\\venv\\Scripts\pyside2-rcc.exe qrc\\badminapp.qrc -o badminapp_rc.py")
#else:
#    os.system('pyside2-rcc qrc/badminapp.qrc -o badminapp_rc.py')

os.system('ls -lrt ui')
