import unittest
from unittest import mock

from game_engine.component.component import Component
from tests.helper import patcher

from game_engine.actor.actor import Actor
from game_engine.display_configuration import DisplayConfiguration
from game_engine.event.event import Event
from game_engine.game import Game
from game_engine.geometry.point import Point3D
from game_engine.geometry.vector import Vector3D

event_handler_mock = mock.MagicMock()


class TestActor(unittest.TestCase):
    def setUp(self):
        patcher.start_patch(self, 'game_engine.game.Game')
        self.display_configuration = mock.MagicMock()
        self.display_configuration.fps = 30
        self.Game.display_configuration.return_value = self.display_configuration
        self.test_actor = DummyActor()

    def tearDown(self):
        patcher.stop_patches()

    def test_creating_actor_at_default_position(self):
        an_actor = Actor()

        assert Point3D(0, 0, 0) == an_actor.position

    def test_changing_actor_position(self):
        an_actor = Actor()

        an_actor.position = Point3D(3, 2, 1)

        assert Point3D(3, 2, 1) == an_actor.position

    def test_raise_type_error_when_invalid_position_object_provided_to_actor(self):
        an_actor = Actor()

        self.assertRaises(TypeError, an_actor.position, 'something')

    def test_executing_callback_for_subscribed_event(self):
        test_event = TestEvent()

        self.test_actor.receive_event(test_event)

        event_handler_mock.assert_called_once_with(test_event)

    def test_doing_nothing_for_non_subscribed_event(self):
        test_event = AnotherTestEvent()

        self.test_actor.receive_event(test_event)

        event_handler_mock.assert_not_called()

    def test_actor_position_changes_on_tick_notification_when_on_move_vector_is_not_zero_normalized_with_the_fps(self):
        Game.set_display_configuration(DisplayConfiguration(800, 600, 30))
        an_actor = Actor()
        an_actor.position = Point3D(5, 5, 5)
        an_actor.move_vector = Vector3D(15, -15, 30)

        an_actor.end_tick()

        assert an_actor.position == Point3D(5.5, 4.5, 6)

    def test_setting_actor_to_added_component(self):
        component1 = mock.MagicMock()

        self.test_actor.add_component(component1)

        assert component1.actor == self.test_actor

    def test_getting_all_components(self):
        component1 = mock.MagicMock()
        component2 = mock.MagicMock()

        self.test_actor.add_component(component1)
        self.test_actor.add_component(component2)

        assert [component1, component2] == self.test_actor.components()

    def test_getting_components_by_class(self):
        component1 = ComponentClass1()
        component2 = ComponentClass2()

        self.test_actor.add_component(component1)
        self.test_actor.add_component(component2)

        assert [component1] == self.test_actor.components(by_class=ComponentClass1)
        assert [component2] == self.test_actor.components(by_class=ComponentClass2)

    def test_notifying_all_components_on_tick_end(self):
        component1 = mock.MagicMock()
        component2 = mock.MagicMock()
        self.test_actor.add_component(component1)
        self.test_actor.add_component(component2)

        self.test_actor.end_tick()

        component1.end_tick.assert_called_once()
        component2.end_tick.assert_called_once()


class TestEvent(Event):
    pass


class AnotherTestEvent(Event):
    pass


class DummyActor(Actor):
    def __init__(self):
        super().__init__()
        self.subscribe_to_event(TestEvent, self.event_handler)

    def event_handler(self, event):
        event_handler_mock(event)


class ComponentClass1(Component):
    def end_tick(self):
        pass


class ComponentClass2(Component):
    def end_tick(self):
        pass
