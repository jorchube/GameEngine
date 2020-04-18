from game_engine.backend.pygameOpenGL.event_converter.event_converter import EventConverter
from game_engine.event.event_type import key_event
import pygame as pg

_pygame_key_event_data_table = {
    pg.K_UP: key_event.Key.UP_ARROW,
    pg.K_DOWN: key_event.Key.DOWN_ARROW,
    pg.K_LEFT: key_event.Key.LEFT_ARROW,
    pg.K_RIGHT: key_event.Key.RIGHT_ARROW,
    pg.K_w: key_event.Key.W,
    pg.K_a: key_event.Key.A,
    pg.K_s: key_event.Key.S,
    pg.K_d: key_event.Key.D,
}


class KeyPressEventConverter(EventConverter):
    @classmethod
    def convert(cls, event):
        if event.key not in _pygame_key_event_data_table:
            print('Unable to convert pygame backend key press event for key {k}'.format(k=event.key))
            return None
        data = _pygame_key_event_data_table[event.key]
        return key_event.KeyEventPress(data)


class KeyReleaseEventConverter(EventConverter):
    @classmethod
    def convert(cls, event):
        if event.key not in _pygame_key_event_data_table:
            print('Unable to convert pygame backend key release event for key {k}'.format(k=event.key))
            return None
        data = _pygame_key_event_data_table[event.key]
        return key_event.KeyEventRelease(data)

