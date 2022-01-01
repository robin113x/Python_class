#!/bin/python3

class Test:
    def __init__(self):
        print('constructor')

    def m1(self):
        print('Method')

t=Test()
t.m1()
t.__init__()
t.__init__()

'''
constructor overloading not supported in python
if someone creat overloaded constructor then latest or last one is valid only
'''
