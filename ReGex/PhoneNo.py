#!/bin/python3
'''
1. Every number should contains exactly 10 digits
2. The first digit should be 7 or 8 or 9
'''
import re
n=(input('Enter 10-Digit mobile no : '))

m=re.fullmatch('[6-9]\d{9}',n)

if m!=None:
    print('Valid Mobile no : ',n)
else:
    print('Invalid no ')



