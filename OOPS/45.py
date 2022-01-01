#!/bin/python3

from os import system as sy
sy('bash info.sh')

class P:
    def property(self):
        print('Power paisa')

    def marry(self):
        print('Marry with xyz')
        
class Child(P):
    def marry(self):
        super().marry()
        print('Marry with aaabbbccc')

ch=Child()
ch.property()
ch.marry()

