import unittest
from unittest import mock

from game_engine import scene


class TestDisplayConfiguration(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_add_actor_to_scene(self):
        test_actor = mock.MagicMock()

        test_scene = scene.Scene()
        test_scene.add_actor(test_actor)

        assert test_actor in test_scene.actors()
