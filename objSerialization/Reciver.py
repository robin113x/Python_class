#!/bin/python3
from Employee import *
import pickle

f1=open('emp1.ser','rb') 
print('Deserialize Emp data & Printing Data')

while True:
    try:
        emp=pickle.load(f1)
        emp.Display()
    except :
        f1.close()
        break

print('All Data completed')


