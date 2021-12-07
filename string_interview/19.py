#!/bin/python3
'''
lazy = zaly ->anagram
'''
s1 = input('Enter the 1st string : ')
s2 = input('Enter the 2nd string : ')

if sorted(s1) == sorted(s2):
    print('The strings are Anagram ')
else:
    print("i'm sorry Babu :(")

