#!/bin/python3

s1=input('Enter any string  : ')
s2=input('Enter any string  : ')

i,j=0,0
output=''

while i<len(s1) and j<len(s2):
    output=output+s1[i]+s2[j]
    i=i+1
    j=j+1

while i<len(s1):
    output = output+s1[i]
    i+=1
while j<len(s2):
    output = output+s2[j]
    j+=1

print(output)

#2nd python code


s1=input('Enter any string  : ')
s2=input('Enter any string  : ')

i,j=0,0
out=''

while i<len(s1) or j<len(s2):
    if i<len(s1):
        out=out+s1[i]
        i+=1
    if j<len(s2):
        out+=s2[j]
        j+=1

print(out)





















