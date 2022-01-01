#!/bin/python3

from zipfile import *

f=ZipFile('Robin.zip','w',ZIP_DEFLATED)
f.write('10.py')
f.write('1.py')
f.write('11.py')
f.write('13.py')
print("ZIP file Created successfully")


    