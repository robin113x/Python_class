#!/bin/python3
from os import system as sy
sy('bash bash.sh')

f1=open('input.txt','r')
f2=open('out.txt','w')

data=f1.read()
f2.write(data)
f1.close()
f2.close()
