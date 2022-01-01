#!/bin/python3

class Car:
    def __init__(self,Name,motor,color):
        self.name=Name
        self.motor=motor
        self.color=color

    def getInfo(self):
        print('Name : ',self.name)
        print('Motor : ',self.motor)
        print('Colour : ',self.color)

class Employee:

    def __init__(self,name,idno,car):
        self.name=name
        self.idno=idno
        self.car=car

    def empinfo(self):
        print('Name  : ',self.name)
        print('Id No : ',self.idno)
        print('Car info')
        self.car.getInfo()


car = Car('BMW','volkswagen','Red')
emp = Employee('robin',114,car)
emp.empinfo()

