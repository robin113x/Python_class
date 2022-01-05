#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

#shallow copy and Deep Copy:

import copy
l1=[10,20,[30,40],50]
print(l1)
l2=copy.copy(l1)
l1[2][0]=888
print(l1)
print(l2)

l3=copy.deepcopy(l1)
l1[2][1]=222
l3[2][0]=30
print(l3)
print(l1)


