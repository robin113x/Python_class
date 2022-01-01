#!/bin/python3
from os import system as sy
sy('clear')
sy('echo "Hello Robin"')


class SportsNews:
    def sinfo(self):
        print('S info 1')
        print('S info 2')
        print('S info 5')
        print('S info 3')
        print('S info 4')

class MoviesNews:
    def minfo(self):
        print('S info 1')
        print('S info 2')
        print('S info 5')
        print('S info 3')

class PoliticsNews:
    def pinfo(self):
        print('S info 1')
        print('S info 2')
        print('S info 5')
        print('S info 3')


class RobinNews:
    def __init__(self):
        self.sports=SportsNews()
        self.movies=MoviesNews()
        self.politics=PoliticsNews()

    def getTotalNews(self):
        print('Welcome to RObin News Network')
        self.sports.sinfo()
        print()
        self.movies.minfo()
        print()
        self.politics.pinfo()


rNews=RobinNews()
rNews.getTotalNews()

