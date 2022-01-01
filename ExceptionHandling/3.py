#!/bin/python3
from os import system as sy
sy('bash bash.sh')

try:
    print('Hello')
    print(10/0)
    print('esxdfs')
except (ZeroDivisionError,ValueError,OverflowError) as e:
    print(e)

except:
    print('Default except')

