import unittest

from game_engine.actor import Actor
from game_engine.component.move_component import MoveComponent, MoveComponentNode
from game_engine.display.display_configuration import DisplayConfiguration
from game_engine.game import Game
from game_engine.geometry import Vector3D


class TestParticle(unittest.TestCase):
    def setUp(self):
        Game.set_display_configuration(DisplayConfiguration(800, 600, 1))

    def test_applying_move_component_with_one_node_to_actor(self):
        actor = Actor()
        node = MoveComponentNode(Vector3D(10, 0, 0), 2)
        actor.add_component(MoveComponent([node]))

        actor.end_tick()

        assert actor.move_vector == Vector3D(10, 0, 0)

    def test_applying_move_component_with_many_nodes_to_actor(self):
        actor = Actor()
        node1 = MoveComponentNode(Vector3D(10, 0, 0), 2)
        node2 = MoveComponentNode(Vector3D(0, 5, 0), 2)
        actor.add_component(MoveComponent([node1, node2]))

        actor.end_tick()
        actor.end_tick()
        actor.end_tick()

        assert actor.move_vector == Vector3D(0, 5, 0)

    def test_keep_last_applied_move_component_node(self):
        actor = Actor()
        node1 = MoveComponentNode(Vector3D(10, 0, 0), 2)
        node2 = MoveComponentNode(Vector3D(0, 5, 0), 2)
        actor.add_component(MoveComponent([node1, node2]))

        actor.end_tick()
        actor.end_tick()
        actor.end_tick()
        actor.end_tick()

        assert actor.move_vector == Vector3D(0, 5, 0)

