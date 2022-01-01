#!/bin/python3
from os import system as sy
sy('bash bash.sh')

try:
    print('Hello')
    print(10/0)
    print('Robin')
except ZeroDivisionError:
    print(10/1)

print('neha')

