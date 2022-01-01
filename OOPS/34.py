#!/bin/python3

from os import system as sy
sy('bash info.sh')

class Parent:
    def m1(self):
        print('Parent method')

class Child1(Parent):
    def m2(self):
        print('child1 method')

class Child2(Parent):
    def m3(self):
        print('child2 method')


cc1=Child1()
cc1.m1()
cc1.m2()

cc2=Child2()
cc2.m1()
cc2.m3()
