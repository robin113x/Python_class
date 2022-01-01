#!/bin/python3

class Student:
    '''
    cls --> it is reference to class level object, with the help of cls we can access class level data

    '''
    school="St.albert's High School"

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def getInfo(self): #instance method 
        print('Name',self.name)
        print('Roll',self.roll)

    @classmethod               #class Decorators important 
    def schoolinfo(cls):       # class level method 
        print(cls.school)
        print(id(cls))

    @staticmethod            #general utitlity method is known as static method
    def m1(x,y):
        return x+y

s1=Student('robin',114)
s1.getInfo()
s1.schoolinfo()
res=s1.m1(10,20)
print(res)
print(id(Student))

