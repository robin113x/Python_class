#!/bin/pyhton3

n = int(input('Enter the value of n : '))

for i in range(n):
    print('* '*(i+1))


print()
print('Optimized way')

for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()

