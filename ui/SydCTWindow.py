import syd
import os
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from .ui_SydCTWindow import Ui_SydCTWindow


class SydCTWindow(QWidget, Ui_SydCTWindow):

    def __init__(self, data, filename, table_name):
        super().__init__()
        self._data = data
        self._filename = filename
        self.table_name = table_name
        self.setupUi(self)
        self.button_ct_on.clicked.connect(self.slot_ct_on)
        self.button_ct_off.clicked.connect(self.slot_ct_off)
        self.button_ct_on.setEnabled(False)

    def slot_ct_on(self):
        if len(self._data) < 1:
            print("Aucun élément sélectionné")
        else:
            path = []
            for d in self._data:
                if self.table_name == 'DicomSeries' or self.table_name == 'DicomSeries_default':
                    if d['modality'] == 'CT':
                        print("This is already a CT")
                        db = syd.open_db(self._filename)
                        path.append([self.get_file_path(db, d), 0])
                    else:
                        db = syd.open_db(self._filename)
                        e = self.get_ct_path(db, d)
                        if e is not None:
                            path.append([self.get_file_path(db, d), e])
                        else:
                            path.append([self.get_file_path(db, d), 0])
                elif self.table_name == 'Image' or self.table_name == 'Image_default':
                    print('')

        if len(path) == 1:
            if path[0][1] != 0:
                cmd = f'vv {path[0][1]} --fusion {path[0][0]}'
            else:
                cmd = f'vv {path[0][0]}'
        elif len(path) > 1:
            el = [p[0] for p in path]
            el = ' '.join(el)
            cmd = f'vv {el}'

        os.system(cmd)
        self.hide()

    def slot_ct_off(self):
        if len(self._data) < 1:
            print("Aucun élément sélectionné")
        else:
            path = []
            for d in self._data:
                if self.table_name == 'DicomSeries' or self.table_name == 'DicomSeries_default':
                    db = syd.open_db(self._filename)
                    path.append(self.get_file_path(db, d))
                elif self.table_name == 'Image' or self.table_name == 'Image_default':
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
        self.hide()

    def get_file_path(self, db, d):
        dicom_file = syd.find_one(db['DicomFile'], dicom_series_id=d['id'])
        file = syd.find_one(db['File'], id=dicom_file['file_id'])
        return db.absolute_data_folder + '/' + file['folder'] + '/' + file['filename']

    def get_ct_path(self, db, d):
        path = None
        e = syd.syd_find_ct(db, d['id'])
        if len(e) < 1:
            return path
        else:
            im = None
            dicom_id = e[0][0]
            image_id = e[0][1]
            ct = syd.find_one(db['DicomSeries'], id=dicom_id)
            path = self.get_file_path(db, ct)
            if image_id != 0:
                im = syd.find_one(db['Image'], id=image_id)
                file_mhd_id = im['file_mhd_id']
                file = syd.find_one(db['File'], id=file_mhd_id)
                path = db.absolute_data_folder + '/' + file['folder'] + '/' + file['filename']
                return path

        return path
