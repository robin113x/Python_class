#!/bin/python3

'''
1 EMP NAme
2 emp idno
3 emp salary
4 emp city
5 emp mobile no
6 Designation
'''
from random import *

alphabets = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
cities = ['Hyderabad', 'Chennai', 'Bangalore', 'Pune', 'Delhi', 'Mumbai']
designations = ['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Lead', 'Project Manager']


def getName():
    name = choice(alphabets).upper()
    n = randint(2, 9)
    for i in range(n):
        name += choice(alphabets)
    return name


def idNo():
    eidno = 'e-'
    for i in range(4):
        eidno += choice(digits)
    return eidno


def esalary():
    esal = uniform(10000, 50000)
    return esal


def city():
    ecity = choice(cities)
    return ecity


def fake_no():
    no = choice('9876')
    for i in range(9):
        no += choice(digits)
    return no


def fake_designation():
    designation = choice(designations)
    return designation


def get_fake_emp_data():
    print(' Name : ', getName())
    print(' Id-no : ', idNo())
    print(' Salary :  {:.2f}'.format(esalary()))
    print(' city : ', city())
    print(' Contact : ', fake_no())
    print(' Designations : ', fake_designation())


n = int(input(' Enter the Count : '))
for i in range(n):
    print('*' * 20)
    get_fake_emp_data()
    print()
