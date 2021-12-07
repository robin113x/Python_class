#!/bin/python3

n = int(input('Enter the n  : '))

for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end=' ')
    print()
