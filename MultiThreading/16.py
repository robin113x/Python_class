#!/bin/python3
from os import system as sy
sy('clear')
sy('date')
from threading import *
import time


e=Event()
def trafficpolice():
    while True:
        time.sleep(10)
        print("Green Signal")
        e.set()
        time.sleep(20)
        print("Red Signal")
        e.clear()

def Driver():
    num=0
    while True:
        print("Waiting for Green Signal")
        e.wait()
        print("Go Green")
        while e.is_set():
            num+=1
            print("vehical no : ",num,"Crossing the signal")
            time.sleep(2)
        
        print("RED SIGNAL :(")

t1=Thread(target=trafficpolice)
t2=Thread(target=Driver)
t1.start()
t2.start()