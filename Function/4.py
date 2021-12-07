#!/bin/python3
'''
Returning Multiple values from a function
'''
def calci(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div

t=calci(20,10)
print(type(t))
print(t)

a,b,c,d = calci(40,20)
print(a,b,c,d)

