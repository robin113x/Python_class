#!/bin/python3
from os import system as sy
sy('clear')

from threading import *


def Display():
    for i in range(5):
        print(current_thread().getName())
        print('Child Thread')

for i in range(5):
    print('Main Thread')
    print(current_thread().getName())

t=Thread(target=Display)
t.start()

t1=Thread(target=Display).start()




