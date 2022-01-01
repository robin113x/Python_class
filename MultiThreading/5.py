#!/bin/python3
from os import system as sy
sy('clear')
sy('echo MultiThreaeding ')
sy('echo " "')

from threading import *

def double1(no):
    for i in no:
        print(2*i,' Double ')
        
def square1(no):
    for i in no:
        print('square : ',i*i)


number=[1,2,3,4,5]

th1=Thread(target=double1,args=(number,))
th2=Thread(target=square1,args=(number,))
th1.start()
th2.start()
th1.join()
th2.join()


