#!/bin/python3

'''
i/p- DURGA-SOFTWARE
o/p- A-2
     E-1
     I-0
     O-1
     U-1
'''

s = input('Enter the string : ')

d={}
v={'a','e','i','o','u','A','E','I','O','U'}

for ch in s:
    if ch in v:
        d[ch] = d.get(ch,0)+1

for k,v in d.items():
    print('{} occurse {} times'.format(k,v))

