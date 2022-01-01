#!/bin/python3
from os import path, system as sy
sy('bash bash.sh')

fname=input('Enter file name : ')

res = path.isfile(fname)

if res:
    with open(fname,'r') as f:
        print(f.read())
else:
    print("I am sorry babu ")