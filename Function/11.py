#!/bin/python3
'''
filter with lambda function
'''
names = ['robin','anshu','divya','jayant','hood']
print(names)
out = list(filter(lambda name : len(name)%5==0,names))
print(out)

odd = list(filter(lambda name: len(name)%2!=0,names))
print(odd)

