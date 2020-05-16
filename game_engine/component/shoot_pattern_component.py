from game_engine.component.component import Component
from game_engine.game import Game


class ShootPatternComponentNode(object):
    def __init__(self, particle_emitter_instance, duration_seconds):
        self.particle_emitter_instance = particle_emitter_instance
        self.duration_seconds = duration_seconds


class ShootPatternComponent(Component):
    def __init__(self, shoot_pattern_node_list):
        super().__init__()
        self.__current_tick = 0
        self.__next_node_at_tick = 0
        self.__shoot_pattern_node_list = shoot_pattern_node_list
        self.__current_shoot_pattern_node = None

    def end_tick(self):
        if self.__is_change_node_tick():
            self.__apply_next_pattern_node()
        if self.__current_shoot_pattern_node and self.__current_shoot_pattern_node.particle_emitter_instance:
            self.__current_shoot_pattern_node.particle_emitter_instance.end_tick()
        self.__current_tick += 1

    def draw(self):
        pass

    def __is_change_node_tick(self):
        return self.__current_tick >= self.__next_node_at_tick

    def __apply_next_pattern_node(self):
        if self.__shoot_pattern_node_list:
            self.__current_shoot_pattern_node = self.__shoot_pattern_node_list.pop(0)
            self.__configure_pattern_node(self.__current_shoot_pattern_node)
            self.__next_node_at_tick = self.__current_tick + (self.__current_shoot_pattern_node.duration_seconds * Game.display_configuration().fps)
        else:
            self.__current_shoot_pattern_node = None

    def __configure_pattern_node(self, node):
        if node.particle_emitter_instance:
            node.particle_emitter_instance.actor = self.actor
