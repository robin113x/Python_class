#!/bin/python3

n = int(input('Enter the value of n '))

for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))

for i in range(n-1):
    print(' '*(i+1)+(str(n-i-1)+' ')*(n-1-i))

