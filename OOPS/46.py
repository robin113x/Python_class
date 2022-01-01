#!/bin/python3

from os import system as sy
sy('bash info.sh')

class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)

class Child(Parent):

    def __init__(self, name, age,roll,marks):
        super().__init__(name, age)
        self.roll=roll
        self.marks=marks

    def display(self):
        super().display()
        print(self.roll)
        print(self.marks)

ch =Child('Robin',20,114,99)
ch.display()

        
