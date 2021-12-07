#!/bin/python3

n = int(input('Enter the value of n : '))

for i in range(n):
    print((str(chr(64+n-i)+' ')*(n-i)))
