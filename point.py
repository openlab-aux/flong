class Point(object):
    def __init__(self, pos_x, pos_y):
        self.__pos_x = pos_x
        self.__pos_y = pos_y

    def move(self, x, y):
        self.__pos_x += x
        self.__pos_y += y

    def setpos(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        self.__pos_x = x

    def set_y(self, y):
        self.__pos_y = y

    def get_x(self):
        return self.__pos_x

    def get_y(self):
        return self.__pos_y