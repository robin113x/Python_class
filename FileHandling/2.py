#!/bin/python3
from os import system as sy
sy('bash bash.sh')


'''
r-read 
w-write (overwrite)
a-append
x-exclude
r+ = read+write
w+=write+read
a+=append+read

'''

f=open('abc.txt','r')

f=open('abc.txt','w')

f=open('abc.txt','a')

f=open('abc.txt','r+')

f=open('abc.txt','w+')

f=open('abc.txt','a+')

f=open('abc.txt','x')

f.close()
