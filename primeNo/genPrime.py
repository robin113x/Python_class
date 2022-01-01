#!/bin/python3

n = int(input('Enter a no : '))

n1=2

while n1<=n:
    isPrime = True
    for i in range(2,n1//2+1):
        if n1%i==0:
            isPrime=False
            break
    if isPrime==True:
        print(n1)
    n1+=1
