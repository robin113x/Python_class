#!/bin/python3
from os import system as sy
sy('bash bash.sh')
#python program

def squareIt(x):
    return x**x

assert squareIt(4)==16,'The sq of 4 is 16'
print(squareIt(4))

