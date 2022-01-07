#!/bin/python3

l1 = eval(input('Enter the list  : '))
print(l1)
s1 = set(l1)
print(s1)
print(list(s1))


l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)


