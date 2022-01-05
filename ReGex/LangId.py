#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

'''
Write a Regular Expression to represent all Yava language identifiers
1. The allowed characters are a-z,A-Z,0-9,#
2. The first character should be a lower case alphabet symbol from a to k
3. The second character should be a digit divisible by 3
4. The length of identifier should be atleast 2
'''
#[a-k][369][a-zA-Z0-9#]*
import re
s=input('Enter Identifiers to Validate : ')
m=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
if m!=None:
    print('Yes it is valid identifiers')
else:
    print(' Not valid ')


