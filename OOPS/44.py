#!/bin/python3

from os import system as sy
sy('bash info.sh')

class Test:
    def m1(self,x):
        print( x.__class__.__name__)

t=Test()
t.m1(41)

