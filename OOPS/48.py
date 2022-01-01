#!/bin/python3

from os import system as sy
sy('bash info.sh')
from abc import abstractmethod,ABC

class Test(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass

    def m3(self):
        print('Hello m3')
        return None

class Child(Test):
    def m1(self):
        print('Hello m1')
        return None

    def m2(self):
        print('Hello m2')
        return None

c=Child()
c.m1()
c.m2()
c.m3()

