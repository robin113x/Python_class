#!/bin/python3

from os import system as sy
sy('bash info.sh')
from abc import abstractmethod,ABC

class Test(ABC):
    @abstractmethod
    def getNoOfWheel(self):
        pass

class BUS(Test):
    def getNoOfWheel(self):
        return 6

class Auto(Test):
    def getNoOfWheel(self):
        return 3

b=BUS()
print(b.getNoOfWheel())

a=Auto()
print(a.getNoOfWheel())


