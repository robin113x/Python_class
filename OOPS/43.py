#!/bin/python3

from os import system as sy
sy('bash info.sh')

class Book:
    def __init__(self,pg):
        self.pg=pg

    def __add__(self,other):
       return Book(self.pg+other.pg)

    def __str__(self):
       return '  Total no of Pg {} '.format(self.pg)

    def __mul__(self,other):
       return Book(self.pg*other.pg)

b1=Book(1)
b2=Book(2)
b3=Book(3)
b4=Book(4)
print(b1+b2+b3+b4)
print(b1+b2*b3+b4)
