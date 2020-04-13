class Rotation(object):
    def __init__(self, x=0, y=0, z=0, rotation_callback=None):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__cb = rotation_callback

    def __callback(self):
        if self.__cb:
            self.__cb()

    @property
    def x_axis(self):
        return self.__x

    @x_axis.setter
    def x_axis(self, degrees):
        self.__x = self.__normalize_degrees(degrees)
        self.__callback()

    @property
    def y_axis(self):
        return self.__y

    @y_axis.setter
    def y_axis(self, degrees):
        self.__y = self.__normalize_degrees(degrees)
        self.__callback()

    @property
    def z_axis(self):
        return self.__z

    @z_axis.setter
    def z_axis(self, degrees):
        self.__z = self.__normalize_degrees(degrees)
        self.__callback()

    def __normalize_degrees(self, degrees):
        return degrees % 360


