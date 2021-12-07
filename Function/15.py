#!/bin/python3
from functools import reduce
n = int(input('Enter the range : '))
l = [x for x in range(1,n+1)]
print(l)
out = reduce(lambda x,y:x+y,l)
print(out)

print('Sum of 100 natural no')

add = reduce(lambda x,y:x+y,range(1,101))
print(add)

