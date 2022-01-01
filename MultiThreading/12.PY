#!/bin/python3

from os import system as sy

sy('clear')
sy('date')

from threading import *
import time

l=Lock()
def Wish(name):
    l.acquire()  
    print("Hello : ",name)
    time.sleep(2)
    print(" Welcome to Pyhton World ")
    l.release()

t1=Thread(target=Wish,args=('Robin',))
t2=Thread(target=Wish,args=('Neha',))
t1.start()
t2.start()