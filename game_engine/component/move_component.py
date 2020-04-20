from game_engine.component.component import Component
from game_engine.game import Game


class MoveComponentNode(object):
    def __init__(self, movement_vector, time_seconds):
        self.movement_vector = movement_vector
        self.time_seconds = time_seconds


class MoveComponent(Component):
    def __init__(self, move_component_node_list):
        super().__init__()
        self.__move_node_list = move_component_node_list
        self.__current_tick = 0
        self.__next_node_at_tick = 0

    def end_tick(self):
        if self.__move_node_list and self.__is_change_move_node_tick():
            self.__apply_next_move_node()
        self.__current_tick += 1

    def __apply_next_move_node(self):
        node = self.__move_node_list.pop(0)
        self.actor.move_vector = node.movement_vector
        self.__next_node_at_tick = self.__current_tick + (node.time_seconds * Game.display_configuration().fps)

    def __is_change_move_node_tick(self):
        return self.__current_tick >= self.__next_node_at_tick

