#!/bin/python3

from sys import argv

f1 = open(argv[1])
f2 = open(argv[2])

f3 = open(argv[3],'w')

for x in f1:
    f3.write(x)

for x in f2:
    f3.write(x)


