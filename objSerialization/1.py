#!/bin/python3

from os import system as sy
sy('clear')
sy('date')
import pickle

class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.no=eno
        self.name=ename
        self.sal=esal
        self.address=eaddr

    def Display(self):
        print(f'Id : {self.no} \nName : {self.name}  \nsalary : {self.sal} \nAddress :{self.address} ')


emp =Employee(114,'Robin',20000000,'Patna')
emp.Display()

#Serialization or Pickleing
with open('emp.ser','wb') as f:
    pickle.dump(emp,f)
print('Serialization completed')

#deSerialization or unPickleing
with open('emp.ser','rb') as f:
    Empobj=pickle.load(f)
    
print('deSerialization completed')
Empobj.Display()



