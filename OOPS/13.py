#!/bin/python3

class Test:
    '''various place where instance var is declared
        3 place where instance var is decalred

        1. Inside constructor ---> by using self ref 
        2.Inside instance method ---> by using self ref
        3.outside the class using obj ref var
    '''
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30
        self.d=40

t=Test()
t.m1()
t.e=50
print(t.__dict__)

#How to access instance variable
#Ans --> by using self ref and by using obj ref var

class Test1:
    
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30
        self.d=40
        print(self.a,self.b,self.c,self.d)
        del self.d
        print(self.a,self.b,self.c)

t=Test1()
t.m1()
t.e=50
print(t.a,t.b,t.c,t.e)
del t.a,t.b,t.c
print(t.__dict__)

