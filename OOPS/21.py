#!/bin/python3
#Nested method ---> only in python not supported in java


class Test:

    def m1(self):
        print('Nested method')
        def calci(a,b):
            print(a+b)
            print(a*b)
            print(a-b)
            print(a%b)

        calci(12,10)
        calci(20,3)

t1=Test()
t1.m1()

