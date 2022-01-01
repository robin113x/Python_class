#!/bin/python3

class Students:
    ''' This class for understanding constructors '''
    def __init__(self,name,rollno,marks):
        self.name = name
        self.roll = rollno
        self.marks = marks

    def talk(self):
        print('my name is ',self.name)
        print('my roll is ',self.roll)
        print('my marks is ',self.marks)

s1 = Students('Neha',138,99)
s2 = Students('Robin',144,99)
s1.talk()
s2.talk()
