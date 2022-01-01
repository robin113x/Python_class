#!/bin/python3

class Students:
    school_name = "St.Albert's High School"  # school_name is static variable

    def __init__(self, name, roll):
        self.name = name  # name and roll is instance variable
        self.roll = roll

    def m1(self):
        x = 10  # x & i is local variable
        for i in range(x):
            print(i)


if __name__ == '__main__':
    s1 = Students('robin', 114)
    s1.m1()
