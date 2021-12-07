#!/bin/python3

print('Greater between three no :')

a = int(input(' Enter the 1st no '))
b = int(input(' Enter the 4th no '))
c = int(input(' Enter the 3rd no '))

if a>b and a>c:
    print('{}= is Greater'.format(a))

elif b>a and b>c:
    print('{}= is Greater'.format(b))

else:
    print('{}= is Greater'.format(c))

