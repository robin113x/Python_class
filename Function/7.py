#!/bin/python3

def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
n=int(input('Enter the no : '))
x=fact(n)
print('Factorial of {} is = {} '.format(n,x))

