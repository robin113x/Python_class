#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

def smartDiv(func):
    def inner(x,y):
        if x ==0 or y==0:
            print("I'm Sorry babu :)")
        else:
            func(x,y)
    return inner


@smartDiv
def Division(a,b):
    print(a/b)

Division(10,5)
Division(5,0)
Division(0,852)

