#!/bin/python3

from os import system as sy
sy('clear')
sy('bash info.sh')


class Parent:
    def m1(self):
        print('parent class method')

class Child(Parent):
    def m2(self):
        print('child class method')

class subChild(Child):
    def m3(self):
        print('sub child class method')

sc = subChild()
sc.m1()
sc.m2()
sc.m3()

