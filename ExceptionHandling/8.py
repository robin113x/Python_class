#!/bin/python3
from os import system as sy
sy('bash bash.sh')

try:
    print('Try block')
    a=10/0
    
except Exception as e:
    print(e)
    print('Exception block')

else:
    print('Try run successfully')

finally:
    print('clean up code')

