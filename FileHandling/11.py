#!/bin/python3
from os import system as sy
sy('bash bash.sh')

with open('abc.txt','r') as f:
    print(f.read(2))
    print(f.tell())
    print(f.read(5))
    print(f.tell())
    f.seek(2)
    print(f.tell())
    f.seek(500)
    print(f.tell())
