#!/bin/python3
from os import path, system as sy
sy('bash bash.sh')

f1 = open('RObin.jpg','rb')
data = f1.read()
print(type(data))
f2 = open('kohinoor.jpg','wb')
f2.write(data)