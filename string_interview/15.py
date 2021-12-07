#!/bin/python3
'''
count frequency of char in 
a string 
'''
s=input('Enter the string : ')
d={}
for ch in s:
    d[ch]=d.get(ch,0)+1


for k,v in d.items():
    print(k,' ',v)



