import unittest
from unittest import mock

from src.game_engine.game import Game
from tests.helper import patcher
from src.game_engine.engine import engine
from src.game_engine import display_configuration


class TestEngine(unittest.TestCase):
    def setUp(self):
        patcher.start_patch(self, 'src.game_engine.collision_engine.CollisionEngine')
        self.collision_engine = mock.MagicMock()
        self.CollisionEngine.return_value = self.collision_engine
        self.engine_delegate = mock.MagicMock()
        self.test_engine = DummyEngine(display_configuration.DisplayConfiguration(800, 600, 60), mock.MagicMock(), self.engine_delegate)

    def tearDown(self):
        patcher.stop_patches()

    def test_creating_engione_should_update_game_globals(self):
        assert Game.display_configuration() == self.test_engine.display_configuration

    def test_should_create_display_configuration(self):
        display_config = display_configuration.DisplayConfiguration(800, 600, 30)
        assert 800 == display_config.width
        assert 600 == display_config.height
        assert 30 == display_config.fps

    def test_calling_engine_delegate_initialize_when_creating_engine(self):
        self.engine_delegate.initialize.assert_called_once()

    def test_calling_engine_delegate_end_tick_when_calling_run_loop(self):
        self.test_engine._run_loop()
        self.engine_delegate.end_tick.assert_called_once()

    def test_calling_engine_delegate_clear_display_when_calling_run_loop(self):
        self.test_engine._run_loop()
        self.engine_delegate.clear_display.assert_called_once()

    def test_should_calculate_scene_actors_collisions_on_run_loop(self):
        scene, actor_list = given_test_scene()
        self.test_engine.set_scene(scene)

        self.test_engine._run_loop()

        self.collision_engine.calculate_collisions.assert_called_once_with(actor_list)

    def test_should_calculate_scene_actors_collisions_of_new_scene_on_run_loop(self):
        scene, actor_list = given_test_scene()
        another_scene, another_actor_list = given_test_scene()
        self.test_engine.set_scene(scene)

        self.test_engine._run_loop()
        self.test_engine.set_scene(another_scene)
        self.test_engine._run_loop()

        self.collision_engine.calculate_collisions.assert_has_calls([
            mock.call(actor_list),
            mock.call(another_actor_list)
        ])

    def test_should_process_events_on_run_loop(self):
        self.test_engine._run_loop()

        assert self.test_engine.process_events_called

    def test_calling_engine_delegate_to_clear_display_and_notify_end_tick_on_run_loop(self):
        pass


def given_test_scene():
    scene = mock.MagicMock()
    actor = mock.MagicMock()
    actor_list = [actor]
    scene.actors.return_value = actor_list
    return scene, actor_list


class DummyEngine(engine.Engine):
    def __init__(self, display_configuration, scene, engine_delegate):
        super().__init__(display_configuration, scene, engine_delegate)
        self.ticks = 0
        self.process_events_called = False

    def _end_tick(self):
        self.ticks += 1

    def _process_events(self):
        self.process_events_called = True

