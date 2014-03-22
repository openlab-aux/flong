#!/usr/bin/env python2
from point import Point
from gameobject import GameObject
from ball import Ball
from char import Char


class GameBoard(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__border_min = Point(0, 0)
        self.__border_max = Point(self.__x, self.__y)
        self.__board = []
        self.gameobj = []
        self.gameobj.append(GameObject(Point(1, 4), self.__border_min, self.__border_max, 6, 1))
        self.gameobj.append(GameObject(Point(78, 4), self.__border_min, self.__border_max, 6, 1))
        self.gameobj.append(Ball(Point(40, 7), self.__border_min, self.__border_max, 1, 1, self.gameobj))
        self.mkboard()

    def mk_cleanboard(self):
        self.__board = []
        for y in range(0, self.__y):
            line = []
            for x in range(0, self.__x):
                line.append(0)
            self.__board.append(line)

    def mkboard(self):
        self.mk_cleanboard()
        self.gameobj[2].updatepos()
        for item in self.gameobj:
            for idx, line in enumerate(item.area):
                self.__board[line[1]][line[0]] = 1

    def mk_scorebard(self):
        self.mk_cleanboard()
        scorechars = []
        scorechars.append(Char(Point(27, 4), Point(0, 0), Point(0, 0), self.gameobj[0].score))
        scorechars.append(Char(Point(36, 4), Point(0, 0), Point(0, 0), 10))
        scorechars.append(Char(Point(45, 4), Point(0, 0), Point(0, 0), self.gameobj[1].score))
        for item in scorechars:
            for idx, line in enumerate(item.area):
                self.__board[line[1]][line[0]] = 1

    def get_board(self):
        return self.__board
