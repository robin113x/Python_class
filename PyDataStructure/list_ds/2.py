#!/bin/python3

''' Creation of list object'''

#empty list object

l=[]
print(type(l))

#if we know data
l=[10,20,30,40,50]
print(l)

#dynamic input

l=eval(input('Enter the list : '))
print(type(l))
print(l)

#by using list()-> function

l=list('Robin')
print(l)

l=list(range(0,10,2))
print(l)


#by using split function
w='learning python is very easy'
l=w.split()
print(l)




