#!/bin/python3

import time

class Test:
    def __init__(self):
        print("Obj initialization")

    def __del__(self):
        print('Cleanup code')

t=Test()
t=None
time.sleep(10)
print('Thank u')

