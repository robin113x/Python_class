#!/bin/python3

import threading

def Display():
    print('This is my 1st threading classs',threading.current_thread().getName())

t=threading.Thread(target=Display)
t.start()

print('MAin Thread',threading.current_thread().getName())

