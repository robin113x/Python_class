#!/bin/python3

from os import system as sy

sy('clear')
sy('date')

from threading import *
import time


def display():
    for i in range(5):
        print(i)
        print(current_thread().name)
        print(current_thread().daemon)


t = Thread(target=display, name="ROBIN",daemon=True)
print(t.daemon)
 
t.start()
print('*'*10)
print(current_thread().getName())
print(current_thread().isDaemon())

time.sleep(1)
