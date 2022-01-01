#!/bin/python3

n=int(input('Enter the n : '))

n1=2
c=0
while True:
    isPrime=True
    for i in range(2,n1//2+1):
        if n1%i==0:
            isPrime=False
            break
    if isPrime==True:
        print(n1)
        c+=1
    if c==n:
        break
    n1+=1
