#!/bin/python3

print('Lesser between three no :')

a = int(input(' Enter the 1st no '))
b = int(input(' Enter the 2th no '))
c = int(input(' Enter the 3rd no '))

if a<=b and a<c:
    print(' {}= is lesser'.format(a))

elif b<a and b<=c:
    print(' {}= is lesser'.format(b))

else:
    print(' {}= is lesser'.format(c))

