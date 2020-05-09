from game_engine.event import event_handler
from game_engine import game
from game_engine.geometry.point import Point3D
from game_engine.geometry.vector import Vector3D
from game_engine.geometry.rotation import Rotation


class Actor(object):
    def __init__(self):
        self.__position = Point3D(0, 0, 0)
        self.__move_vector = Vector3D(0, 0, 0)
        self.__rotation = Rotation(rotation_callback=self.__rotation_callback)
        self.__spinning_speed = 0
        self.__event_handler = event_handler.EventHandler()
        self.__components = []
        self.__collision_mask = 0x0

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

    @property
    def rotation(self):
        return self.__rotation

    @property
    def spinning_speed(self):
        return self.__spinning_speed

    @spinning_speed.setter
    def spinning_speed(self, z_axis):
        self.__spinning_speed += z_axis

    @property
    def collision_mask(self):
        return self.__collision_mask

    @collision_mask.setter
    def collision_mask(self, mask):
        self.__collision_mask = mask

    def end_tick(self):
        self.__update_position()
        if self.__spinning_speed != 0:
            self.rotation.z_axis += self.__spinning_speed
        for component in self.__components:
            component.end_tick()

    def draw(self):
        for component in self.__components:
            component.draw()

    def __update_position(self):
        self.position = self.position + self.__move_vector_per_tick()

    def __move_vector_per_tick(self):
        return Vector3D.divide_vector_by_number(self.move_vector, game.Game.display_configuration().fps)

    def __rotation_callback(self):
        for component in self.__components:
            component.update_rotation()
