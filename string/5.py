#!/bin/python3

mail = input('Enter your mail : ')

try:
    i=mail.index('@')
    print('valid mail')
except ValueError:
    print('invalid mail')


