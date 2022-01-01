How to check a particular file exists or not?
=============================================
We can use os library to get information about files  in our computer. We can check whether a particular file exists or not by using isfile() function.

                os.path.isfile(fname)

Q1. Write a  program to check whether the given file exists or not. If it is available then print its content?

import os
fname=input('Enter File Name:')
if os.path.isfile(fname):
	print('File Exists:',fname)
	print('The Content of the File is:')
	f=open(fname,'r')
	text=f.read()
	print('*'*40)
	print(text)
	print('*'*40)
	f.close()
else:
	print('File does not exist:',fname)


Q2. Program to print the number of lines,words and characters present in the given file?

import os
fname=input('Enter File Name:')
if os.path.isfile(fname):
	print('File Exists:',fname)
	f=open(fname,'r')
	lcount=ccount=wcount=0
	for line in f:
		lcount=lcount+1
		ccount=ccount+len(line)
		words_in_current_line=line.split()
		wcount=wcount+len(words_in_current_line)
	print('The Number Of Lines:',lcount)
	print('The Number Of Characters:',ccount)
	print('The Number Of Words:',wcount)
else:
	print('File does not exist:',fname)

import os
fname=input('Enter File Name:')
if os.path.isfile(fname):
	lcount=wcount=ccount=0
	f=open(fname,'r')
	for line in f:
		lcount=lcount+1
		number_of_words_in_current_line=len(line.split())
		wcount=wcount+number_of_words_in_current_line
		number_of_characters_in_current_line=len(line)
		ccount=ccount+number_of_characters_in_current_line
	print('The Number of Lines:',lcount)
	print('The Number of words:',wcount)
	print('The Number of Characters:',ccount)
else:
	print('File does not exist:',fname)


Handling Binray Data:
--------------------
It is very common requirement to read or write binary data like images,video files,audio files etc.

Program to read image file and write to a new image file:
---------------------------------------------------------
f1=open('guido.jpg','rb')
imagebytes=f1.read()
#print(type(imagebytes))
f2=open('durgasoftguido.jpg','wb')
f2.write(imagebytes)
print('New Image is available with the name:durgasoftguido.jpg')
f1.close()
f2.close()
