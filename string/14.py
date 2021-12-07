#!/bin/python3

s=input('Enter any string : ')

if s.isalnum():
    print('Alpha numeric  : ')
elif s.isalpha():
    print('all alpha:')
elif s.isdigit():
    print('all digit ' )
elif s.isspace():
    print('all space')
elif s.islower():
    print('all lower')
elif s.isupper():
    print('all upper')
elif s.istitle():
    print('all title')
else:
    print('invalid')

