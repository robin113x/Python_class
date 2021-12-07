#!/bin/python3

s = input('Enter any string : ')
l = s.split()
l1=[]
for word in l:
    l1.append(word[::-1])

print(l1)
out = ' '.join(l1)
print(out)
