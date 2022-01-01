#!/bin/python3
from os import system as sy
sy('bash info.sh')

class Parent:
    def __init__(self):
        print('Parent class')

    def m1(self):
        print('Parent m1')

class Child(Parent):
    def __init__(self):
        print('Child class')

    def m2(self):
        print('Child m2')

ch=Child()
ch.m1()
ch.m2()










