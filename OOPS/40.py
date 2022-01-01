#!/bin/python3

from os import system as sy
sy('bash info.sh')

class Book:
    def __init__(self,pg):
        self.pg=pg

    def __add__(self,other):
        total_pg=self.pg+other.pg
        return total_pg

b1=Book(100)
b2=Book(300)
print(b1+b2)
'''
magic operator

'''
