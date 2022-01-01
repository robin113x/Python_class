#!/bin/python3
from os import system as sy
sy('bash bash.sh')

f=open('abc.txt','r')

list1=f.readlines()

for i in list1:
    print(i,end='')