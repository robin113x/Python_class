#!/bin/python3
from os import system as sy
sy('clear')
sy('echo MultiThreaeding ')
sy('echo " "')

from threading import *
class Test:
    def display(self):
        for i in range(4):
            print(current_thread().getName())
            print('Child thread')

obj=Test()
t=Thread(target=obj.display)
t.start()

