#!/bin/python3
from os import system as sy
sy('clear')
sy('date')

class Emplyee:
    def __init__(self,eid,name,sal):
        self.eid=eid
        self.name=name
        self.sal=sal

    def Display(self):
        print(f'Id : {self.eid} \nName : {self.name}  \nsalary : {self.sal} \n ')


