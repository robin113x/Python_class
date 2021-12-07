#!/bin/python3

n=int(input('Enter the value of n : '))

for i in range(n):
    print(' '*i,end='')
    for j in range(n-i):
        print(str(chr(64+n-j)),end=' ')
    print()

