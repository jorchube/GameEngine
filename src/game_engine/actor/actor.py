from src.game_engine.event import event_handler
from src.game_engine import game
from src.game_engine.geometry.point import Point3D
from src.game_engine.geometry.vector import Vector3D
from src.game_engine.geometry.operations import GeometryOperations


class Actor(object):
    def __init__(self):
        self.__position = Point3D(0, 0, 0)
        self.__move_vector = Vector3D(0, 0, 0)
        self.__event_handler = event_handler.EventHandler()
        self.__components = []

    def add_component(self, component):
        component.actor = self
        self.__components.append(component)

    def components(self, by_class=None):
        if by_class is None:
            return self.__components
        return self.__components_by_class(by_class)

    def __components_by_class(self, by_class):
        return list(filter(lambda component: component.__class__ == by_class, self.__components))

    def subscribe_to_event(self, event_type, callback):
        self.__event_handler.subscribe(event_type, callback)

    def receive_event(self, event):
        self.__event_handler.event(event)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if new_position.__class__ == Point3D:
            self.__position = new_position
        else:
            raise TypeError('Actor position needs to be a {needed} was {was}'.format(needed=Point3D.__name__, was=new_position.__class__.__name__))

    @property
    def move_vector(self):
        return self.__move_vector

    @move_vector.setter
    def move_vector(self, new_vector):
        if new_vector.__class__ == Vector3D:
            self.__move_vector = new_vector
        else:
            raise TypeError('Actor vector needs to be a {needed} was {was}'.format(needed=Vector3D.__name__, was=new_vector.__class__.__name__))

    def end_tick(self):
        self.__update_position()
        for component in self.__components:
            component.end_tick()

    def __update_position(self):
        self.position = self.position + self.__move_vector_per_tick()

    def __move_vector_per_tick(self):
        return Vector3D.divide_vector_by_number(self.move_vector, game.Game.display_configuration().fps)

