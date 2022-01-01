#!/bin/python3
import time
from os import system as sy
sy('clear')
sy('echo MultiThreaeding ')
sy('echo " "')

from threading import *

def Display():
    print(current_thread().name)
    time.sleep(2)
    print(current_thread().name)

t1=Thread(target=Display,name='CHildThread')
t2=Thread(target=Display,name='CHildThread')
t3=Thread(target=Display,name='CHildThread')
t4=Thread(target=Display,name='CHildThread')
t5=Thread(target=Display,name='CHildThread')
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

l=enumerate()

for i in l:
    print('Thread Name :',i.name)

time.sleep(2)
l=enumerate()
for i in l:
    print('Thread Name :',i.name)