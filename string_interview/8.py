#!/bin/python3

s=input('Enter the string : ')
alpha=[]
digit=[]

for ch in s:
    if ch.isalpha():
        alpha.append(ch)
    else:
        digit.append(ch)

sort1 = sorted(alpha)
sort2 = sorted(digit)

out = ''.join(sort1+sort2)
print(out)




