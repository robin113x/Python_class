#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

from threading import *
import time
import random
items=[]

def produce(c):
    while True:
        c.acquire()
        item=random.randint(1, 100)
        print("producing the item  : ",item)
        items.append(item)
        print('Producer giving notification...')
        c.notify()
        c.release()
        time.sleep(3)

def Consumer(c):
    while True:
        c.acquire()
        print("Consumer waiting.....")
        c.wait()
        print('Consumer consuming the item',items.pop())
        c.release()
        time.sleep(3)

c=Condition()
t1=Thread(target=produce,args=(c,))
t2=Thread(target=Consumer,args=(c,))
t1.start()
t2.start()