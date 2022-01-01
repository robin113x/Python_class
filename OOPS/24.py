#!/bin/python3

class Engine:
    def m1(self):
        print('this is Engine Function')


class Car:
    def __init__(self):
        self.engine = Engine()

    def m2(self):
        print('This is M2 function')
        self.engine.m1()

c=Car()
c.m2()

