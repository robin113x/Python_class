#!/bin/python3

def AddDecor(func):
    def inner(x,y):
        print('*'*20)
        print(f'Sum Of {x} & {y} is  ',end='')
        func(x,y)
    return inner

@AddDecor
def add(a,b):
    print(a+b)

add(10,20)

