#!/bin/python3
from os import system as sy
sy('clear')
sy('echo MultiThreaeding ')
sy('echo " "')

from threading import *
print(current_thread().getName())
current_thread().setName('Robin')
print(current_thread().getName())
print(current_thread().name)
