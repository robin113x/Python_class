#!/bin/python3
from os import system as sy
sy('bash bash.sh')

fname=input('Enter file name : ')
f=open(fname,'r')

data=f.read()
print(data)
data=f.read(3)
print(data)
data=f.readline()
print(data)
data=f.readlines()
print(data)
data=f.close()

