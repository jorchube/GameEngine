class Polygon(object):
    def __init__(self, point_list):
        if len(point_list) < 3:
            raise PolygonConstructionError('Insufficient points to draw a polygon')
        self.__point_list = point_list

    @property
    def point_list(self):
        return self.__point_list

    @property
    def center(self):
        from src.game_engine.geometry.operations import GeometryOperations
        return GeometryOperations.polygon_center(self)

    def translate(self, vector):
        self.__point_list = [point + vector for point in self.point_list]

    def __repr__(self):
        ret = '{Polygon (self) :'.format(self=self)
        for point in self.__points:
            ret = ret + ' {0}'.format(point)
        ret = ret + '}'
        return ret


class PolygonConstructionError(RuntimeError):
    pass