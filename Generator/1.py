#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

g=(x*x for x in range(100000000000000000000000))

while True:
    print(next(g))

