#!/bin/python3

n = int(input('Enter the range : '))

l1 = [x for x in range(1,n+1)]
l2 = [x+n for x in range(1,n+1)]
l3 = [x+n+n for x in range(1,n+1)]
print(l1)
print(l2)
print(l3)
out = list(map(lambda x,y,z : x+y+z,l1,l2,l3))
print(out)


