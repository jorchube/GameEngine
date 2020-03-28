import unittest
from unittest import mock

from src.game_engine.actor.actor import Actor
from src.game_engine.actor.draw_actor_delegate import DrawActorDelegate
from src.game_engine.display_configuration import DisplayConfiguration
from src.game_engine.event.event import Event
from src.game_engine.game import Game
from src.game_engine.geometry.point import Point3D
from src.game_engine.geometry.vector import Vector3D

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

    def test_calling_draw_delegate_when_drawing_actor(self):
        draw_delegate = DummyDrawActorDelegate()
        an_actor = Actor(draw_delegate)

        an_actor.draw()

        assert draw_delegate.draw_called_with_actor == an_actor

    def test_actor_position_changes_on_tick_notification_when_on_move_vector_is_not_zeroes_normalized_with_the_fps(self):
        Game.set_display_configuration(DisplayConfiguration(800, 600, 30))
        draw_delegate = DummyDrawActorDelegate()
        an_actor = Actor(draw_delegate)
        an_actor.position = Point3D(5, 5, 5)
        an_actor.move_vector = Vector3D(15, -15, 30)

        an_actor.end_tick()

        assert an_actor.position == Point3D(5.5, 4.5, 6)


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


class DummyDrawActorDelegate(DrawActorDelegate):
    def __init__(self):
        self.draw_called_with_actor = None

    def draw(self, actor):
        self.draw_called_with_actor = actor
