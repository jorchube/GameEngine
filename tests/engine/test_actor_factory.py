import unittest
from unittest import mock

from src.game_engine import backend
from src.game_engine.actor.actor_factory import ActorFactory
from src.game_engine.actor.player_actor import PlayerActor
from src.game_engine.actor.polygon_actor import PolygonActor
from tests.helper import patcher


class TestActorFactory(unittest.TestCase):
    def setUp(self):
        backend.polygon_actor_draw_delegate = mock.MagicMock()

    def tearDown(self):
        patcher.stop_patches()

    def test_creating_a_polygon_actor(self):
        point_list = ['point1', 'point2', 'point3']

        actor = ActorFactory.new_polygon_actor(point_list)

        assert actor.__class__ == PolygonActor
        assert actor.points == point_list
        backend.polygon_actor_draw_delegate.assert_called_once()

    def test_creating_a_player_actor(self):
        point_list = ['point1', 'point2', 'point3']

        actor = ActorFactory.new_player_actor(point_list)

        assert actor.__class__ == PlayerActor
        assert actor.points == point_list
        backend.polygon_actor_draw_delegate.assert_called_once()