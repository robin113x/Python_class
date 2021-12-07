#!/bin/python3

s=input('enter a string ')

l=s.split()
rev = l[::-1]
print(rev)
out = ' '.join(rev)
print(out)

