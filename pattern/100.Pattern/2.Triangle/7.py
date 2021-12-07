#!/bin/python3

n=int(input('Enter the value of n : '))

for i in range(n):
    for j in range(i+1):
        print(chr(64+n-j), end =' ')
    print()
