from src.game_engine.actor import actor


class PolygonActor(actor.Actor):
    def __init__(self, polygon=None, draw_delegate=None):
        self.__polygon = polygon
        super().__init__(draw_delegate)

    @property
    def polygon(self):
        return self.__polygon

    @property
    def hitbox(self):
        return self.__polygon

