#!/bin/python3

class Person:
    def __init__(self,name,age):
        print('Parent constructor')
        self.name=name
        self.age=age

    def eatdrink(self):
        print('Eating Biryani & Drink Coca~cola')

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def work(self):
        print('Coding Python Program')

    def empInfo(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)

emp =Employee('Robin',21,114,200000000)
emp.eatdrink()
emp.work()
emp.empInfo()

