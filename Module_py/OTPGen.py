#!/bin/python3
from random import *
'''
OTP Generator
'''
otp=''

for i in range(6):
    otp=otp+str(randint(0,9))

print(' OTP : ',otp) 


print('Alpha Numeric OTP ')

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit = '0123456789'

otp=''

for i in range(3):
    otp=otp+choice(alpha)+choice(digit)
print(' OTP : ',otp)
