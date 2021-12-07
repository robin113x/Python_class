#!/bin/python3

n = int(input('Enter a no : '))

for i in range(n):
    print(str(chr(65+i)+' ')*(i+1))

