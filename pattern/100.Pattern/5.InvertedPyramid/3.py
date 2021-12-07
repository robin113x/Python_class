#!/bin/python3

n = int(input('Enter the value of n : '))

for i in range(n):
    print(' '*i+(str(chr(65+i))+' ')*(n-i))

