#!/bin/python3

def Decor(func):
    def inner():
        print('Send the person to Beauty Parlour')
        print('Showing this person with full of Decorator')

    return inner

@Decor
def Display():
    print('Showing a person as it is')


Display()



