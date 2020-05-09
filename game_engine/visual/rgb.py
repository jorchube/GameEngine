import random


class RGB(object):
    def __init__(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green

    @property
    def blue(self):
        return self.__blue

    @red.setter
    def red(self, value):
        self.__red = value

    @green.setter
    def green(self, value):
        self.__green = value

    @blue.setter
    def blue(self, value):
        self.__blue = value

    @classmethod
    def random(cls):
        return RGB(
            random.randint(0, 10) * 0.1,
            random.randint(0, 10) * 0.1,
            random.randint(0, 10) * 0.1,
        )
