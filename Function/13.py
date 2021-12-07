#!/bin/python3

#map with multiple function

n = int(input('Enter the range : '))
l1 = [x for x in range(1,n+1)]
print(l1)
l2 = [x+n for x in range(1,n)]
print(l2)

out = list(map(lambda x,y:x+y,l1,l2))
print(out)



















