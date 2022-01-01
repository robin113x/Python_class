#!/bin/python3
from os import system as sy
sy('bash bash.sh')

def temp():
    l=[]
    for i in range(5):
        s=input('Enter name  : ')
        l.append(s)
    print(l)

temp()

