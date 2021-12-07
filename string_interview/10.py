#!/bin/python3


s=input('Enter any string : ')

output=''

for ch in s:
    if ch.isalpha():
        x=ch
    else:
        output=output+x*int(ch)

l1 = ''.join(sorted(output))
print(l1)

