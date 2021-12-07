#!/bin/python3

s=input('Enter the string ')

output=''
i=len(s)-1

while i>=0:
    output=output+s[i]
    i-=1
print(output)

