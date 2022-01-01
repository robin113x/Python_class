#!/bin/python3

class Test:
    def __init__(self):
        print('Address of Object pointed by self : ',id(self))

t = Test()
print('Address of Object pointed by t :    ',id(t))

