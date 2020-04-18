import unittest
from unittest import mock

from game_engine.event import event_handler
from game_engine.event import event


class TestEventHandler(unittest.TestCase):
    def setUp(self):
        self.test_event = event.Event()
        self.test_event_2 = event.Event()
        self.test_callback = mock.MagicMock()
        self.test_callback_2 = mock.MagicMock()

    def tearDown(self):
        pass

    def test_should_execute_callback_for_subscribed_event_type_when_handling_one_event(self):
        handler = event_handler.EventHandler()
        handler.subscribe(event.Event, self.test_callback)

        handler.event(self.test_event)

        self.test_callback.assert_called_once_with(self.test_event)

    def test_should_execute_many_callback_for_subscribed_event_type_when_handling_one_event(self):
        handler = event_handler.EventHandler()
        handler.subscribe(event.Event, self.test_callback)
        handler.subscribe(event.Event, self.test_callback_2)

        handler.event(self.test_event)

        self.test_callback.assert_called_once_with(self.test_event)
        self.test_callback_2.assert_called_once_with(self.test_event)

    def test_should_execute_callback_for_subscribed_event_type_when_handling_many_events(self):
        handler = event_handler.EventHandler()
        handler.subscribe(event.Event, self.test_callback)

        handler.event(self.test_event)
        handler.event(self.test_event_2)

        self.test_callback.assert_has_calls([
            mock.call(self.test_event),
            mock.call(self.test_event_2),
        ])
