#!/bin/python3
from os import system as sy
sy('clear')

class Parent:
    def m1(self):
        print('Parent method')

class Child(Parent):
    def m2(self):
        print('Child Method')

ch = Child()
ch.m1()
ch.m2()

