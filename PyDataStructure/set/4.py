#!/bin/python3

vowels = {'a','e','i','o','u'}
word = input('Enter the Word  : ')
word1 = word.lower()
print(word1)
s=set(word1)

res=s.intersection(vowels) # s&vowels
print(res)





