#!/usr/bin/env python2
from point import Point


class GameObject(object):
    def __init__(self, position, border_min, border_max, length, width):
        self.position = position
        self.border_min = border_min
        self.border_max = border_max
        self.length = length
        self.width = width
        self.area = []
        self.gen_area()
        self.hitstatus = 0
        self.score = 0

    def gen_area(self):
        self.area = []
        for w in range(0, self.width):
            for l in range(0, self.length):
                line = [self.position.get_x() + w, self.position.get_y() + l]
                self.area.append(line)

    def _set_x(self, x, area_flag):
        if self.border_min.get_x() <= x <= self.border_max.get_x():
            if self.border_min.get_x() <= x + self.width <= self.border_max.get_x():
                self.position.set_x(x)
                if area_flag is True:
                    self.gen_area()
            else:
                self.hitstatus = 5
                return 0
        else:
            self.hitstatus = 5
            return 0  # horizontal

    def _set_y(self, y, area_flag):
        if self.border_min.get_y() <= y <= self.border_max.get_y():
            if self.border_min.get_y() <= y + self.length <= self.border_max.get_y():
                self.position.set_y(y)
                if area_flag is True:
                    self.gen_area()
            else:
                self.hitstatus = 23
                return 0
        else:
            self.hitstatus = 23
            return 0  # vertical

    def move(self, x, y):
        self._set_x(self.get_x() + x, False)
        self._set_y(self.get_y() + y, True)

    def _setpos(self, x, y):
        self._set_x(x, False)
        self._set_y(y, True)

    def get_x(self):
        return self.position.get_x()

    def get_y(self):
        return self.position.get_y()
