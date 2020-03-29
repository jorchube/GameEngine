class Rotation(object):
    def __init__(self, rotation_callback):
        self.__x = 0
        self.__y = 0
        self.__z = 0
        self.__callback = rotation_callback

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


