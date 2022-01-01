#!/bin/python3
from os import system as sy
sy('bash bash.sh')

try:
    print(10/0)
except Exception as e:
    print(type(e))
    print(e.__class__)
    print(e.__class__.__name__)
    print(e)


