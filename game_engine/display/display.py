import math

from game_engine.display.display_configuration import DisplayConfiguration
from game_engine.geometry import Point3D


class Display(object):
    __configuration = None

    @classmethod
    def set_configuration(cls, configuration):
        if type(configuration) != DisplayConfiguration:
            raise DisplayError('Unable to set display configuration with an object of type {t}'.format(t=type(configuration)))
        cls.__configuration = configuration

    @classmethod
    def configure(cls, width_px, height_px, fps, scaled=False):
        cls.set_configuration(DisplayConfiguration(width_px, height_px, fps, scaled))

    @classmethod
    def configuration(cls):
        return cls.__configuration

    @classmethod
    def get_width(cls):
        return cls.__configuration.width

    @classmethod
    def get_height(cls):
        return cls.__configuration.height

    @classmethod
    def get_boundaries(cls):
        return DisplayBoundaries(cls)

    @classmethod
    def ratio(cls):
        return cls.__configuration.width/cls.__configuration.height


class DisplayBoundaries(object):
    def __init__(self, display):
        from game_engine.game import Game
        max_y = (math.sin(math.radians(Game.get_camera().fov / 2)) * (math.fabs(Game.get_camera().position.z)))
        max_x = max_y * display.ratio()
        self.__top_left = Point3D(-max_x, max_y, 0)
        self.__top_right = Point3D(max_x, max_y, 0)
        self.__bottom_left = Point3D(-max_x, -max_y, 0)
        self.__bottom_right = Point3D(max_x, -max_y, 0)

    @property
    def top_left(self):
        return self.__top_left

    @property
    def top_right(self):
        return self.__top_right

    @property
    def bottom_left(self):
        return self.__bottom_left

    @property
    def bottom_right(self):
        return self.__bottom_right


class DisplayError(RuntimeError):
    pass