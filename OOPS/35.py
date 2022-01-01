#!/bin/python3

from os import system as sy
sy('bash info.sh')

class P1:
    def m1(self):
        print('m1 from p1')

class P2:
    def m2(self):
        print('m2 from p2')

class Child(P1,P2):
    def m3(self):
        print('m3 from Child')


cc=Child()
cc.m2()
cc.m1()
cc.m3()

