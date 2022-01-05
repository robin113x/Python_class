#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

def Decor1(func):
    def inner1():
        print('Inner 1 Execute')
        func()
    return inner1

def Decor2(func):
    def inner2():
        print('Inner 2 Execute')
        func()
    return inner2

@Decor2
@Decor1 
def fun():
    print('Main Function')

fun()

