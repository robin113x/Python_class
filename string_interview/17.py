#!/bin/python3

'''
i/p-> AAAABBBCCD
O/P-> A4B3C2D1
'''

s=input('Enter the string : ')
d={}
out=''
for ch in s:
    d[ch] = d.get(ch,0)+1

for k,v in d.items():
    out=out+k+str(v)

print(out)

