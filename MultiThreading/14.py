#!/bin/python3

from os import system as sy

sy('clear')
sy('date')

from threading import *
import time
s=Semaphore(3)
def Wish(name):
    s.acquire()
    for i in range(2):
        print("Good Evening : ",name)
        time.sleep(2)
        print(current_thread().name)
    s.release()

t1=Thread(target=Wish,args=('Robin1',))
t2=Thread(target=Wish,args=('Robin2',))
t3=Thread(target=Wish,args=('Robin3',))
t6=Thread(target=Wish,args=('Robin6',))
t4=Thread(target=Wish,args=('Robin4',))
t5=Thread(target=Wish,args=('Robin5',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()