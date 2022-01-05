#!/bin/python3
'''
Write a python program to extract all mobile numbers present in
input.txt where numbers are mixed with normal text data
'''
from os import system as sy
sy('clear')
sy('date')

import re
iFile=input('Enter the input file name : ')
f=open(iFile,'r')
f1=open('output.txt','w')
for line in f:
    list1=re.findall('[6-9]\d{9}',line)
    for no in list1:
        f1.write(no+'\n')

print('All no Added to Output.txt')
f.close()
f1.close()

