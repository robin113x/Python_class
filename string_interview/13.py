#!/bin/python3

s=input('enter the string : ')

l=[]
for ch in s:
    if ch not in l:
        l.append(ch)

print(l)

for ch in l:
    print('{} occurs {} times'.format(ch,s.count(ch)))
   

#2nd way
s=input('enter the string : ')
s1 = set(s)

for ch in s1:
    print('{} occurs {} times'.format(ch,s.count(ch)))
   


