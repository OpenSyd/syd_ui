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
gen_ui(w,  'SydCTWindow')

os.system('ls -lrt ui')
