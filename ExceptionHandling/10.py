#!/bin/python3
from os import system as sy
sy('bash bash.sh')

class TooYoung(Exception):
    def __init__(self,msg):
        self.msg=msg

class TooOld(Exception):
    def __init__(self,msg):
        self.msg=msg

age=int(input('Enter ur age : '))

if age >60:
    raise TooYoung('Wait for some more time : ')

elif age<12:
    raise TooOld('I"m sorry babu ')

else:
    print('Sahi hai !!!!!!!!!!')

