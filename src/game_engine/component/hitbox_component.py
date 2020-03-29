from src.game_engine.component.component import Component


class HitboxComponent(Component):
    def __init__(self, hitbox, is_collision_source=False):
        super().__init__()
        self.__hitbox = hitbox
        self.__is_collision_source = is_collision_source

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
        # TODO: rotate

