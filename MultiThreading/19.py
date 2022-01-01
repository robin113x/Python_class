#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

from threading import *
import time
import random
import queue

def produce(q):
    while True:
        item=random.randint(1, 100)
        print("Produce item : ",item)
        q.put(item)
        print("producer giving notification")
        time.sleep(5)


def consumer(q):
    while True:
        print("Consumer waiting for updation")
        print("consuming item : ",q.get())
        time.sleep(3)


q=queue.Queue()
t1=Thread(target=produce,args=(q,))
t2=Thread(target=consumer,args=(q,))
t1.start()
t2.start()