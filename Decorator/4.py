#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

def Decor(func):
    def inner(name):
        namelist=['Robin','Neha']
        if name in namelist:
            print('*'*35)
            print(f'{name} is Best hacker in the World!')
            print('*'*35)
        else:
            func(name)

    return inner

@Decor
def Wish(name):
    print(f'{name} hello good evening')

Wish('Robin')
Wish('Rishu')
Wish('Neha')



