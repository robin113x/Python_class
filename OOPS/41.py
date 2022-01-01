#!/bin/python3

from os import system as sy
sy('bash info.sh')

class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def __gt__(self,other):
        res=self.mark > other.mark
        return res

s1=Student('RObin',99)
s2=Student('Neha',98)
print(s1>s2)
print(s1<s2)


