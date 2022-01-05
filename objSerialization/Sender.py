#!/bin/python3

from Employee import *
import pickle

f=open('emp1.ser','wb')

while True:
    eid=int(input('Enter id : '))
    ename=input('Enter Name : ')
    sal=float(input('Enter salary : '))
    
    e=Emplyee(eid,ename,sal)
    pickle.dump(e,f)

    opt = input('Do u want to continuee....[Y/N] : ')
    o=opt.lower()
    if o == 'n' or o == 'no':
        break

print('Thank You')


