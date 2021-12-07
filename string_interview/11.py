#!/bin/python3

#ord('a')---> 97
#chr(97)---> a


s=input('Enter the alphanumeric : ')

output=''
for ch in s:
    if ch.isalpha():
        output=output+ch
        x=ch
    else:
        output=output+chr(ord(x)+int(ch))
print(output)

