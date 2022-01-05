#!/bin/python3

def DecorAdd(func):
    def inner(a,b):
        print('*'*30)
        print(f'The sum of {a} and {b} is : ',end='')
        func(a,b)
        print('*'*30)
    return inner
       

@DecorAdd
def Add(x,y):
    print(x+y)


Add(10,20)

