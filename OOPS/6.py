#!/bin/python3

class Students:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.mark=marks

    def m1(self):
        print('Name : ',self.name)
        print('Roll : ',self.roll)
        print('Marks : ',self.mark)

t1 = Students('robin',114,99)
t1.m1()

