import unittest
from unittest import mock

from game_engine.scene import scene


class TestDisplayConfiguration(unittest.TestCase):
    def setUp(self):
        self.display = mock.MagicMock()
        self.test_scene = scene.Scene(self.display)

    def tearDown(self):
        pass

    def test_should_add_actor_to_scene(self):
        test_actor = mock.MagicMock()

        self.test_scene.add_actor(test_actor)

        assert test_actor in self.test_scene.actors()

    def test_should_remove_actor_from_scene(self):
        test_actor = mock.MagicMock()
        self.test_scene.add_actor(test_actor)

        self.test_scene.remove_actor(test_actor)

        assert test_actor not in self.test_scene.actors()
