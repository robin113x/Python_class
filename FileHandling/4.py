#!/bin/python3
from os import system as sy
sy('bash bash.sh')

f=open('abc.txt','w+')

f.write('Robin\n')
f.writelines('Neha is Gf of robin : cute couple \n ')

f.close()
print('data Write successfully')

