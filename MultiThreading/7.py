#!/bin/python3
from os import system as sy
sy('clear')
sy('echo MultiThreaeding ')
sy('echo " "')

from threading import *

class Test(Thread):
    def run(self):
        print("Child Thread identification no :",current_thread().ident)

t=Test()
t.start()
print("Child Thread identification no :",t.ident)
print("MAin Thrread identification no :",current_thread().ident)