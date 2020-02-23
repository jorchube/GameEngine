from src.game_engine.event import event_handler
from src.game_engine.geometry.point import Point3D


class Actor(object):
    def __init__(self, draw_delegate=None):
        self.__position = Point3D(0, 0, 0)
        self.__hitbox = None
        self.__event_handler = event_handler.EventHandler()
        self.__draw_delegate = draw_delegate

    def draw(self):
        self.__draw_delegate.draw(self)

    def subscribe_to_event(self, event_type, callback):
        self.__event_handler.subscribe(event_type, callback)

    def receive_event(self, event):
        self.__event_handler.event(event)

    @property
    def hitbox(self):
        return self.__hitbox

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if new_position.__class__ == Point3D:
            self.__position = new_position
        else:
            raise TypeError('Actor position needs to be a {needed} was {was}'.format(needed=Point3D.__name__, was=new_position.__class__.__name__))