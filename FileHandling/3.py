#!/bin/python3
from os import system as sy
sy('bash bash.sh')

f=open('abc.txt','w+')

print('file name : ',f.name)
print('file mode : ',f.mode)
print('file is closed : ',f.closed)
print('file is readable ',f.readable())
print('file is writeable : ',f.writable())
f.close()
print('file is closed : ',f.closed)


