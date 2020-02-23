class Point3D(object):
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @z.setter
    def z(self, value):
        self.__z = value

    def as_tuple(self):
        return self.__x, self.__y, self.__z

    def __add__(self, other):
        x = self.__x + other.x
        y = self.__y + other.y
        z = self.__z + other.z
        return Point3D(x, y, z)

    def __repr__(self):
        return '({0},{1},{2})'.format(self.__x, self.__y, self.__z)

    def __eq__(self, other):
        return self.as_tuple() == other.as_tuple()
