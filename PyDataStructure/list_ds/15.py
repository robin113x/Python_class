#!/bin/python3

l1=[10,20,30,40]
l2=[30,40,50,60]
print(l1)
print(l2)
l3 = [x for x in l1 if x not in l2]
print(l3)


l4 = [x for x in l1 if x in l2]
print('Union') 
print(l4)



s='the quick brown fox jumps over the lazy dog'
words=s.split()

l=[[word.upper(),len(word)] for word in words]
print(l)

