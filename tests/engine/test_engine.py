import unittest
from unittest import mock

from tests.helper import patcher
from src.game_engine import engine
from src.game_engine import display_configuration


class TestEngine(unittest.TestCase):
    def setUp(self):
        patcher.start_patch(self, 'src.game_engine.collision_engine.CollisionEngine')
        self.collision_engine = mock.MagicMock()
        self.CollisionEngine.return_value = self.collision_engine

    def tearDown(self):
        patcher.stop_patches()

    def test_should_create_display_configuration(self):
        display_config = display_configuration.DisplayConfiguration(800, 600)
        assert 800 == display_config.width
        assert 600 == display_config.height

    def test_should_initialize_engine_and_set_scene(self):
        scene = mock.MagicMock()
        DummyEngine(60, display_configuration.DisplayConfiguration(800, 600), scene)

    def test_should_signal_tick_end_every_run_loop(self):
        scene, actor_list = given_test_scene()
        dummy_engine = DummyEngine(60, display_configuration.DisplayConfiguration(800, 600), scene)

        dummy_engine._run_loop()
        assert 1 == dummy_engine.ticks

        dummy_engine._run_loop()
        assert 2 == dummy_engine.ticks

    def test_should_calculate_scene_actors_collisions_on_run_loop(self):
        scene, actor_list = given_test_scene()
        dummy_engine = DummyEngine(60, display_configuration.DisplayConfiguration(800, 600), scene)

        dummy_engine._run_loop()

        self.collision_engine.calculate_collisions.assert_called_once_with(actor_list)

    def test_should_calculate_scene_actors_collisions_of_new_scene_on_run_loop(self):
        scene, actor_list = given_test_scene()
        another_scene, another_actor_list = given_test_scene()
        dummy_engine = DummyEngine(60, display_configuration.DisplayConfiguration(800, 600), scene)

        dummy_engine._run_loop()
        dummy_engine.set_scene(another_scene)
        dummy_engine._run_loop()

        self.collision_engine.calculate_collisions.assert_has_calls([
            mock.call(actor_list),
            mock.call(another_actor_list)
        ])

    def test_should_process_events_on_run_loop(self):
        scene, actor_list = given_test_scene()
        dummy_engine = DummyEngine(60, display_configuration.DisplayConfiguration(800, 600), scene)

        dummy_engine._run_loop()

        assert dummy_engine.process_events_called


def given_test_scene():
    scene = mock.MagicMock()
    actor = mock.MagicMock()
    actor_list = [actor]
    scene.actors.return_value = actor_list
    return scene, actor_list


class DummyEngine(engine.Engine):
    def __init__(self, framerate, display_configuration, scene):
        super(DummyEngine, self).__init__(framerate, display_configuration, scene)
        self.ticks = 0
        self.process_events_called = False

    def _end_tick(self):
        self.ticks += 1

    def _process_events(self):
        self.process_events_called = True

    def _draw_actors(self, actors):
        for actor in actors:
            actor.draw()
