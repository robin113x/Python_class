#!/bin/python3

l=eval(input('Enter the list : '))
i=0
while (i<len(l)):
    print('The element present at +ve index {} and -ve index {} is {}'.format(i,i-len(l),l[i]))    
    i+=1
