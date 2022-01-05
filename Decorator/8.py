#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

def Decor11(func1):
    def inner11():
        x=func1()
        return x*x
    return inner11

def Decor22(func2):
    def inner22():
        x=func2()
        return 2*x
    return inner22

@Decor11
@Decor22
def fun1():
    return 20

print(fun1())


@Decor22
@Decor11
def fun2():
    return 20

print('*'*20)
print(fun2())