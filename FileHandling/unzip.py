#!/bin/python3

from zipfile import *
f=ZipFile('Robin.zip','r',ZIP_STORED)
name=f.namelist()
print(name)
#f.extractall()
for eachFile in name:
    fi = open(eachFile,'r')
    text = fi.read()
    print("File Name : ",eachFile)
    print('*'*20)
    print(text)
    fi.close()
    print()