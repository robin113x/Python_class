#!/bin/python3
from random import *

while True:
    out = randint(1,9)
    x = int(input(' Guess any no b/w 1 to 9 : '))
    if x==out:
        print(' You won the Match ')
    else:
        print(' Your no is {} and Lucky no {} '.format(x,out))
        print(' Sorry u loose ')
    opt = input(' Do u want to paly again ... [y/n] : ')
    if opt == 'n' or opt =='N':
        break

