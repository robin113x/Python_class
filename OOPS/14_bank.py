#!/bin/python3

class Customer:
    '''This class Developed by Robin Roy'''

    bankname='RobinH00d'

    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
        
    def deposite(self,amount):
        self.balance = self.balance + amount
        print('Net Amount : ',self.balance)

    def withdraw(self,amount):

        if amount > self.balance:
            print('Sorry insufficient Balance')
        else:
            self.balance=self.balance-amount
            print('Net Balance : ',self.balance)

print(' Welcome to ',Customer.bankname)
name=input('Enter the Name: ')
c1 = Customer(name)

while True:
    print(' D - Deposite \n W - Withdraw \n E - exit ')
    optio = input('Enter the option : ')
    opt = optio.lower()
    if opt == 'd':
        amt = eval(input('Enter the amount : '))
        c1.deposite(amt)
    elif opt == 'w':
        amnt = eval(input('Enter the amount to withdraw : '))
        c1.withdraw(amnt)

    elif opt == 'e':
        print(' Thank you ')
        break
    else:
        print('Enter the valid option :')




