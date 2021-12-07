#!/bin/python3

def ifact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

no=int(input('Enter the no : '))
res = ifact(no)
print(res)


print('*'*30)

def recfact(no):
    if no==1 or no ==0:
        return 1
    return no*recfact(no-1)


no=int(input('Enter the no : '))
print(recfact(no))

