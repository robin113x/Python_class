#!/bin/python3

'''
i/p ->  aaaabbbccd
o/p -> 4a3b2c1d
'''

print('Hello')

s=input('Enter the string : ')

previous = s[0]

out=''
c=1
i=1
while i< len(s):
    if s[i] == previous:
        c+=1
    else:
        out=out+str(c)+previous
        previous=s[i]
        c=1
    if i==(len(s)-1):
        out=out+str(c)+previous
        

    i+=1

print(out)

