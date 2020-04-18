from game_engine.component.component import Component
from game_engine.geometry.operations import GeometryOperations


class HitboxComponent(Component):
    def __init__(self, hitbox, is_collision_source=False):
        super().__init__()
        self.__is_collision_source = is_collision_source
        self.__hitbox = hitbox
        self.__original_hitbox = hitbox

    @property
    def hitbox(self):
        return self.__hitbox

    @property
    def is_collision_source(self):
        return self.__is_collision_source

    @is_collision_source.setter
    def is_collision_source(self, value):
        self.__is_collision_source = value

    def end_tick(self):
        pass

    def update_rotation(self):
        super().update_rotation()
        self.__hitbox = GeometryOperations.rotate_polygon(self.__original_hitbox, self.actor.position, self.actor.rotation.z_axis)