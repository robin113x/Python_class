#!/bin/python3
from threading import *
from os import system as sy
sy('clear')
sy('echo MultiThreaeding ')
sy('echo " "')


class Test(Thread):
    def run(self):

        for i in range(3):
            print('Active Count Thread',active_count())
            print(current_thread().name)

t=Test()
t.start()
t.setName("Robin")
print('Active Count Thread',active_count())
print(current_thread().name)