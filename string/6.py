#!/bin/python3

s=input('Enter the string : ')
sub = input('enter the sub string : ')

i=0
print('All sub string ',s.count(sub))

i = s.find(sub)
if i==-1:
    print("i'm sorry babu ")
while i!=-1:
    print('{} found at index {} '.format(sub,i))

    i = s.find(sub,i+len(sub),len(s))
