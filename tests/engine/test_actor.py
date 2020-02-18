import unittest
from unittest import mock

from src.game_engine.actor.actor import Actor
from src.game_engine.event.event import Event
from src.game_engine.geometry.point import Point3D


event_handler_mock = mock.MagicMock()


class TestActor(unittest.TestCase):
    def setUp(self):
        self.test_actor = DummyActor()

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

    def draw(self):
        pass
