from src.game_engine.geometry.operations import GeometryOperations
from src.game_engine.geometry.vector import Vector3D


class Component(object):
    def __init__(self):
        self.__actor = None
        self.__tag = None
        self.__components = []
        self.__offset_relative_to_actor = Vector3D(0, 0, 0)
        self.__original_offset_relative_to_actor = Vector3D(0, 0, 0)

    @property
    def actor(self):
        return self.__actor

    @actor.setter
    def actor(self, actor):
        self.__actor = actor

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    def add_component(self, component):
        component.actor = self
        self.__components.append(component)

    def components(self, by_class=None):
        if by_class is None:
            return self.__components
        return self.__components_by_class(by_class)

    def __components_by_class(self, by_class):
        return list(filter(lambda component: component.__class__ == by_class, self.__components))

    @property
    def position(self):
        return self.actor.position

    @property
    def position_offset_relative_to_actor(self):
        return self.__offset_relative_to_actor

    @position_offset_relative_to_actor.setter
    def position_offset_relative_to_actor(self, vector):
        self.__original_offset_relative_to_actor = vector

    def update_rotation(self):
        self.__offset_relative_to_actor = GeometryOperations.rotate_vector(self.__original_offset_relative_to_actor, self.actor.rotation.z_axis)

    def end_tick(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self == other

    def __ne__(self, other):
        return not self.__eq__(other)
