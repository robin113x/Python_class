#!/bin/python3

d=eval(input('Enter the Dictionary : '))

sum=0
for i in d.values():
    sum+=i
print(sum)

#inbuilt function for sum

print('sum of values : ', sum(d.values()))

