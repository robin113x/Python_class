#!/bin/python

from os import system as sy
sy('bash info.sh')

#Hybrid Inheritance

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

print(D.mro())
print(C.mro())
print(B.mro())
print(A.mro())

