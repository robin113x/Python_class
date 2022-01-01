#!/bin/python3
from os import system,_exit 
system('bash bash.sh')

try:
    print('try')
    _exit(0)
except Exception as e:
    print(e)
finally:
    print('finally block')
