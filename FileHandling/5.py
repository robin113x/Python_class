#!/bin/python3
from os import system as sy
sy('bash bash.sh')

fname=input('Enter file name : ')
f=open(fname,'w')

while True:
    data=input('Enter ur data : ')
    f.write(data+'\n')

    opt=input('Do u want to continue [y/n]: ')
    if opt.lower()=='no' or opt.lower()=='n':
        break

f.close()
print('Thank you')


