#!/bin/python3

s=input('Enter the string : ')

output=''

for ch in s:
    if ch not in output:
        output=output+ch
print(output)


#2nd way

s=input('Enter the string : ')
l=[ ]
for ch in s:
    if ch not in l:
        l.append(ch)
print(l)
out1 = ''.join(l)
print(out1)

#3rd way

s=input('Enter the string : ')

s1 = set(s)
out = ''.join(s1)
print(out)





















