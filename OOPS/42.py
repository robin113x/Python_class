#!/bin/python3

from os import system as sy
sy('bash info.sh')

class Employee:
    def __init__(self,name,salaryperday):
        self.name=name
        self.salaryperday=salaryperday

    def __mul__(self,other):
        money=self.salaryperday*other.workingDay
        return money

    def __str__(self):
        #return self.name
        return 'name {}, salaryperday {} '.format(self.name,self.salaryperday)



class TimeSheet:
    def __init__(self,name,workingDay):
        self.name=name
        self.workingDay=workingDay

e=Employee('Robin',1000000)
t=TimeSheet('Robin',20)
print(e*t)

print(e)
