#!/bin/python3

import re

s=input('ENter the string : ')

l=re.search('^Learn',s,re.IGNORECASE)
l2=re.search('Python$',s,re.IGNORECASE)

if l != None and l2 != None:
    print('String start with learn and End with Python')
else:
    print('Not start')

