#!/bin/python3
from os import system as sy
sy('bash bash.sh')

f=open('abc.txt','r')

line1=f.readline()

while line1 !='':
    print(line1,end='')
    line1=f.readline()



f.close()

print('\nThank you')