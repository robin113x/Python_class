#!/bin/python3
from logging import *
from os import system as sy
sy('bash bash.sh')
# python program
basicConfig(filename='log.txt', level=10,
            format='%(asctime)s: %(name)s : %(levelname)s : %(message)s ', 
            datefmt='%d/%m/%Y %I:%M:%S %p')

info("Stating")
try:
    a =int(input('Enter a no : '))
    b =int(input('Enter a no : '))
    d = a/b
except Exception as msg:
    exception(msg)
    print('Error')
