#!/bin/python3
from os import system as sy
sy('bash bash.sh')

try:
    print('hello')
except:
    print('handling code')
finally:
    print('Thank u')

