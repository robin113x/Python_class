#!/bin/python3
from os import system as sy
sy('clear')
sy('date')
from threading import *
import time

def consumer(c):
    c.acquire()
    print("Consumer waiting for updation...")
    c.wait()
    print("consumer got notification ...")
    c.release()

def produce(c):
    c.acquire()
    print("Producer produce item...")
    c.notify()
    c.release()


c=Condition()
t1=Thread(target=consumer,args=(c,))
t2=Thread(target=produce,args=(c,))
t1.start()
t2.start()
