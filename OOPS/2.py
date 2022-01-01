#!/bin/python3

class Students:
    ''' Functions knows as Method within a class'''
    def __init__(self):   #constructor
        self.name = 'Robin'
        self.roll = 114
        self.marks = 99

    def talk(self):
        print("Hello i'm  :",self.name)
        print("My roll no : ",self.roll)
        print("my marks are :",self.marks)

s=Students()
print(s.name)
print(s.roll)
s.talk()
