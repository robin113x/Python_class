#!/bin/python3
'''
i/p - > AAABAABBC
O/P-> 
'''
s=input('Enter the string : ')
d={}
output=''

for ch in s:
    d[ch]=d.get(ch,0)+1

for k,v in d.items():
    output=output+str(v)+k

print(output)

