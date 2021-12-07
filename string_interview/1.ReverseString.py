#!/bin/python3

s=input('Enter any string ' )
print(s)
rev = s[::-1]
print(rev)

print(type(reversed(s)))

r = reversed(s)
output=''.join(r)
print(output)
