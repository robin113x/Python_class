#!/bin/python3
from os import system as sy
sy('clear')
sy('date')
from threading import *
import time


e=Event()
def Consumer():
    print("Consumer Thread waiting for Updation....")
    e.wait()
    print("Consumer Thread got notification....")

def producer():
    time.sleep(5)
    print("Producer thread producing items")
    print("Producer thread giving notification and consuming items ..")
    e.set()

t1=Thread(target=Consumer)
t2=Thread(target=producer)
t1.start()
t2.start()














