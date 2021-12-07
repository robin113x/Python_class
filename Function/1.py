#!/bin/python3
'''
Function basic
'''

def calculate(a,b):
    print('the sum : ',a+b)
    print('The Diff : ',a-b)
    print('The product : ',a*b)
    print('The devision : ',a/b) #floating --> output
    print('the devide : ',a//b) #not floating output

calculate(10,2)

def wish(name):
    print('Hello {} good Evening :)'.format(name))
wish('Neha')


print('#'*30)

def sqareano(no):
    print(no*no)

n=int(input('Enter a no : '))
sqareano(n)

