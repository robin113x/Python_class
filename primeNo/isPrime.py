#!/bin/python3

n = int(input('Enter a no : '))

if n<=1:
    print('Not a prime no ')
   
elif n==2 or n==3:
    print('prime no')
  
elif n%2==0 or n%3==0:
    print('not prime')

else:
    
    isPrime=True

    for i in range(5,n):
        if n%i==0:
            print('Not prime no')
            isPrime=False
            break

    if isPrime==True:
        print('no is prime')




