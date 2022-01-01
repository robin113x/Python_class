#!/bin/python3
from os import system as sy
sy('bash info.sh')

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eatDrink(self):
        print('Eating Briyani & Drinking Coca~cola')


class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def getinfo(self):
        print('car info {} {} {} '.format(self.name,self.model,self.color))

class Employee(Person):
    def __init__(self,name,age,idno,esal,car):
        super().__init__(name,age)
        self.idno=idno
        self.car=car
        self.esal=esal

    def work(self):
        print('Code python program')


    def empInfo(self):
        print(self.name)
        print(self.age)
        print(self.idno)
        print(self.esal)
        self.car.getinfo()


cc=Car('BMW','volkswagen','red')
emp=Employee('robin',21,114,200000000,cc)
emp.eatDrink()
emp.work()
emp.empInfo()

