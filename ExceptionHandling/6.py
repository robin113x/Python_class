#!/bin/python3
from os import system  
system('bash bash.sh')

try:
    print('try')
    print(10/0)
except Exception as e:
    print(10/2)
    print(e)
finally:
    print('finally block')
