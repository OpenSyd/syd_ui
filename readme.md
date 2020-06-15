SYD is a command-line environment and a python toolkit to perform image processing tasks on a database of medical
 images. It is initially developed to manage SPECT/CT images and perform tasks such as computing activity or
  integrated activity in various ROIs, in the field of Target Radionuclide Therapy and nuclear medicine.  

# syd_ui   
```syd_ui``` is a minimalist GUI to views elements in the database. Start by typing ```syd_ui --db toto.db```. The
 option ```--db``` may be omitted if the ```SYD_DB_FILENAME``` environment variable is set.

It requires: ```syd``` and ```Pyside2``` a python qt module. 

# Development

Run ```make_ui.py``` when one of the ```.ui``` file is modified. Those files describe the GUI and may be created with
 QT designer. 