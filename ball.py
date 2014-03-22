#!/usr/bin/env python2
# coding=utf-8
from gameobject import GameObject
from random import randint


class Ball(GameObject):
    def __init__(self, position, border_min, border_max, length, width, gameobj):
        GameObject.__init__(self, position, border_min, border_max, length, width)
        self.associated_players = gameobj
        self.__speed = 1
        self.__minspeed = 1
        self.__maxspeed = 4
        self.__angle = randint(0, 5)  # 0 = 45°; 1 = 90°; 2 = 135 °; 3 = 225°; 4 = 270; 5 = 315

    def _fset_x(self, x, area_flag):
        for idx in range(0, 2):
            for item in self.associated_players[idx].area:
                if (x is item[0]) and self.get_y() is item[1]:
                    self.hitstatus = 42  # player is the answer
                    return 0
        self._set_x(x, area_flag)

    def _fset_y(self, y, area_flag):
        for idx in range(0, 2):
            for item in self.associated_players[idx].area:
                if self.get_x() is item[0] and self.get_y() is item[1]:
                    self.hitstatus = 42
                    return 0  # return player is the answer
        self._set_y(y, area_flag)

    def bounce(self):
        if self.__angle % 2 is 0:
            self.__angle += 1
        elif self.__angle % 2 is 1:
            self.__angle -= 1
        else:
            self.__angle = 0
        #  self.__angle = randint(0, 5)

    def playerbounce(self):
        if self.__angle is 0:
            self.__angle = 5
        elif self.__angle is 1:
            self.__angle = 4
        elif self.__angle is 2:
            self.__angle = 3
        elif self.__angle is 4:
            self.__angle = 1
        elif self.__angle is 5:
            self.__angle = 0

    def move(self, x, y):
        self._fset_x(self.get_x() + x, False)
        self._fset_y(self.get_y() + y, True)
# 45 -> 135 / 0 -> 1
# 90 -> 270 / 2 -> 3
# 225 -> 315 / 4 -> 5
    def fmove(self):
        if self.__angle == 0:  # 45 °
            self.move(1, -1)
        if self.__angle == 2:  # 90 °
            self.move(1, 0)
        if self.__angle == 1:  # 135 °
            self.move(1, 1)
        if self.__angle == 4:  # 225 °
            self.move(-1, 1)
        if self.__angle == 3:  # 270 °
            self.move(-1, 0)
        if self.__angle == 5:  # 315 °
            self.move(-1, -1)

    def updatepos(self):
        for i in range(0, self.__speed):
            self.fmove()
            if self.hitstatus is 5:
                print "HorizontalBorderHit"
                if self.position.get_x() is self.border_min.get_x():
                    self.associated_players[1].score += 1
                    print "Player 1 Score is:"
                    print self.associated_players[1].score
                if self.position.get_x() is self.border_max.get_x() - 1:
                    self.associated_players[0].score += 1
                    print "Player 0 Score is:"
                    print self.associated_players[0].score
                self.hitstatus = 0
                self._setpos(39, 7)
                self.bounce()
                self.updatepos()
            elif self.hitstatus is 23:
                print "VerticalBorderHit"
                self.hitstatus = 0
                self.bounce()
                self.updatepos()
            elif self.hitstatus is 42:
                print "PlayerHit"
                self.hitstatus = 0
                self.playerbounce()
                self.updatepos()
