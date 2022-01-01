#!/bin/python3
from os import system as sy

sy('clear')
sy('date')

from threading import *
import time


def display():
    print(current_thread().name, "....starting")
    time.sleep(2)
    print(current_thread().name, "....ending")




if __name__ == '__main__':

    t1 = Thread(target=display, name='childThread1')
    t2 = Thread(target=display, name='childThread2')
    t1.start()
    t2.start()

    print(t1.name, "isAlive ", t1.is_alive())
    print(t2.name, "isAlive ", t2.is_alive())
    t1.join()
    t2.join()
    print(t1.name, "isAlive ", t1.is_alive())
    print(t2.name, "isAlive ", t2.is_alive())
