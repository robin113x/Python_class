#!/bin/python3

class Movie:
    ''' This project for understanding constructor'''
    def __init__(self,title,hero,heroine):
        self.name=title
        self.hero=hero
        self.heroine=heroine


    def info(neha):
        print('Movie Name : ',neha.name)
        print('Hero Name : ',neha.hero)
        print('Heroine Name :',neha.heroine)


movie_list=[]
while True:
    title=input('Enter Movie Name : ')
    hero=input('Enter hero name : ')
    heroine=input('Enter heroine name : ')

    m = Movie(title,hero,heroine)
    movie_list.append(m)
    print(' Movie added Successfully ')

    opt = input('Do u want to add new movies [Y/N] : ')
    if opt.lower()=='n':
        break

print('Movie Information  :')

for mov in movie_list:
    mov.info()
    print()


