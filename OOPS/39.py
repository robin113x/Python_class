#!/bin/python3

from os import system as sy
sy('bash info.sh')

class A:
    def m1(self):
        print('a m1')

class B(A):
    def m1(self):
        print('b m1')

class C(B):
    def m1(self):
        print('c m1')


class D(C):
    def m1(self):
        print('d m1')

class E(D):
    def m1(self):
        B.m1(self)
        super(D,self).m1()

ee=E()
ee.m1()
