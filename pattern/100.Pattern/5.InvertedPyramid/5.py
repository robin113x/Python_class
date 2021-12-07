#!/bin/python3

n = int(input('Enter the n : '))

for i in range(n):
    print(' '*i,end='')
    for j in range(n-i):
        print(str(chr(65+j)),end=' ')
    print()
