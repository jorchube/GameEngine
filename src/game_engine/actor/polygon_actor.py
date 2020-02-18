from src.game_engine.actor import actor


class PolygonActor(actor.Actor):
    def __init__(self, point_list=[]):
        if len(point_list) < 3:
            raise PolygonActorConstructionError('Insufficient points to draw a polygon')
        self.__points = point_list
        super().__init__()

    @property
    def points(self):
        return self.__points

    def __repr__(self):
        ret = '{Polygon actor:'
        for point in self.__points:
            ret = ret + ' {0}'.format(point)
        ret = ret + '}'
        return ret


class PolygonActorConstructionError(RuntimeError):
    pass