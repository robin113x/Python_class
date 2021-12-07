#!/bin/python3

def sum(a,b):
    add=a+b
    return add

a = int(input('Enter the 1st no : '))
b = int(input('Enter the 2nd no : '))
res=sum(a,b)
print(res)
sum(85,96)  #-------> No output
print(sum(100,200))

print('*'*20)

#return statements

def fun1():
    print('ByDefault Return Statement ---> None')

x=fun1()
print(x)

