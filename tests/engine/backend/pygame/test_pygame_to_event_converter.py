import unittest

import pygame as pg
from src.game_engine.backend.pygameOpenGL.pygame_to_event_converter import PygameToEventConverter
from src.game_engine.event.event_type import key_event


class TestPygameToEventConverter(unittest.TestCase):
    def test_returns_true_when_can_convert_pygame_event(self):
        assert PygameToEventConverter.can_convert_event(pg.KEYDOWN)

    def test_returns_false_when_can_not_convert_pygame_event(self):
        assert PygameToEventConverter.can_convert_event('Magical event asd asd') is False

    def test_converts_pygame_key_event_to_key_event(self):
        converted_event = PygameToEventConverter.convert(PygameKeyEventTest())

        assert converted_event == key_event.KeyEventPress(key_event.Key.RIGHT_ARROW)


class PygameKeyEventTest(object):
    def __init__(self):
        self.type = pg.KEYDOWN
        self.key = pg.K_RIGHT