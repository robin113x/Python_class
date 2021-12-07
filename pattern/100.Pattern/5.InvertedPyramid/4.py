#!/bin/python3

n = int(input('Enter the n : '))

for i in range(n):
    print(' '*i,end='')
    for j in range(n-i):
        print(j+1,end=' ')
    print()
