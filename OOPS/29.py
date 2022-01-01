#!/bin/python3
from os import system as sy
sy('clear')

class Parent:
    a=10
    def __init__(self):
        print(' Parent Constructor')
        self.b=20

    def m1(self):
        print('Parent Instance Method')

    @classmethod
    def m2(cls):
        print('Parent class Method')

    @staticmethod
    def m3():
        print('Parent static method')

class Child(Parent):
    pass

c1=Child()
c1.m1()
Child.m2()
c1.m3()
print(c1.a)
print(c1.b)

