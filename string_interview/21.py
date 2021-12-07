#!/bin/python2

'''
s1 = 'abcdefg'
s2 = 'xyz'
s3 = '12345'

o/p ->
ax1, by2, cz3, d4, e5, f, g
'''

s1 = input('Enter the string : ') 
s2 = input('Enter the string : ') 
s3 = input('Enter the string : ') 

i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    out=''
    if i<len(s1):
        out=out+s1[i]
        i+=1
    if j<len(s2):
        out=out+s2[j]
        j+=1
    if k<len(s3):
        out=out+s3[k]
        k+=1
    print(out, end=' ')
