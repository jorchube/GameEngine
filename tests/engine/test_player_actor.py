import unittest

from game_engine.event.event_type import key_event
from game_engine.actor.player_actor import PlayerActor
from game_engine.geometry.point import Point3D


class TestPlayerActor(unittest.TestCase):
    def test_should_update_move_vector_when_receiving_arrow_key_press_event(self):
        event = key_event.KeyEventPress(key_event.Key.RIGHT_ARROW)
        actor = PlayerActor()

        actor.receive_event(event)
        actor.end_tick()

        assert Point3D(15, 0, 0) == actor.move_vector
