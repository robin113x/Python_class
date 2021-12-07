#!/bin/python3

s=input('Enter the any string : ')

i=0
for x in s:
    print('char at +ve index = {} and -ve index = {} is {}'.format(i,i-len(s),x))
    i+=1


