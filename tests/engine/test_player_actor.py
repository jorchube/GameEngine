import unittest

from src.game_engine.event.event_type import key_event
from src.game_engine.actor.player_actor import PlayerActor
from src.game_engine.geometry.point import Point3D


class TestPlayerActor(unittest.TestCase):
    def test_should_update_move_vector_when_receiving_arrow_key_press_event(self):
        event = key_event.KeyEventPress(key_event.Key.RIGHT_ARROW)
        actor = PlayerActor([Point3D(1, 0, 0), Point3D(0, 1, 0), Point3D(1, 1, 0)])

        actor.receive_event(event)

        assert Point3D(15, 0, 0) == actor.move_vector
