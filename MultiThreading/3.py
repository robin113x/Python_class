#!/bin/python3
from os import system as sy
sy('clear')
sy('echo MultiThreaeding ')

from threading import *

class MyThread(Thread):
    def run(self):
        for i in range(4):
            print('Child thread')
            print(current_thread().getName())

mt=MyThread()
mt.start()

