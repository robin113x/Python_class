#!/bin/python3

s=input('Enter the string : ')

output=' '

for ch in s:
    if ch.isalpha():
        x=ch
    else:
        output=output+(x*int(ch))

print(output)

