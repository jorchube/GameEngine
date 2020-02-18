from src.game_engine.event.event_type import key_event
import pygame as pg


class PygameToEventConverter(object):
    @classmethod
    def can_convert_event(cls, pygame_event_type):
        return pygame_event_type in cls.__pygame_event_table

    @classmethod
    def convert(cls, pygame_event):
        event_data = cls.__event_data(pygame_event)
        return cls.__create_event(pygame_event, event_data)

    @classmethod
    def __event_data(cls, pygame_event):
        event_table_entry = cls.__pygame_event_table[pygame_event.type]
        return event_table_entry['data'](pygame_event)

    @classmethod
    def __create_event(cls, pygame_event, event_data):
        event_table_entry = cls.__pygame_event_table[pygame_event.type]
        return event_table_entry['event'](event_data)

    __pygame_event_table = {
        pg.KEYDOWN: {
            'event': key_event.KeyEventPress,
            'data': lambda event: PygameToEventConverter.__pygame_key_event_data_table[event.key]
        },
        pg.KEYUP: {
            'event': key_event.KeyEventRelease,
            'data': lambda event: PygameToEventConverter.__pygame_key_event_data_table[event.key]
        },
    }

    __pygame_key_event_data_table = {
        pg.K_UP: key_event.Key.UP_ARROW,
        pg.K_DOWN: key_event.Key.DOWN_ARROW,
        pg.K_LEFT: key_event.Key.LEFT_ARROW,
        pg.K_RIGHT: key_event.Key.RIGHT_ARROW,
    }