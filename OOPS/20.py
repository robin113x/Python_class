#!/bin/python3

class Person:

    def __init__(self,name,dd,mm,yyy):
        print("Person object creation")
        self.dob = self.DOB(dd,mm,yyy)

    def info(self):
        self.dob.display()

    class DOB:
        def __init__(self,dd,mm,yyyy):
            print("DOB object creation")
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy
        
        def display(self):
            print("DOB : {}/{}/{}".format(self.dd,self.mm,self.yyyy))



pp=Person('robin',11,8,2001)

