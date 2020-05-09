import pygame as pg

from game_engine.backend.pygameOpenGL.event_converter.key_event_converter import KeyPressEventConverter
from game_engine.backend.pygameOpenGL.event_converter.key_event_converter import KeyReleaseEventConverter
from game_engine.backend.pygameOpenGL.event_converter.mouse_motion_event_converter import MouseMotionEventConverter
from game_engine.backend.pygameOpenGL.event_converter.quit_event_converter import QuitEventConverter


class PygameToEventConverter(object):
    @classmethod
    def can_convert_event(cls, pygame_event_type):
        if pygame_event_type in cls.__pygame_event_table.keys():
            return True
        # print('Skipping unsupported pygame backend event type: {t}'.format(t=pygame_event_type))
        return False

    @classmethod
    def convert(cls, pygame_event):
        event_converter = cls.__pygame_event_table[pygame_event.type]
        return event_converter.convert(pygame_event)

    __pygame_event_table = {
        pg.KEYDOWN: KeyPressEventConverter,
        pg.KEYUP: KeyReleaseEventConverter,
        pg.QUIT: QuitEventConverter,
        pg.MOUSEMOTION: MouseMotionEventConverter,
        # pg.MOUSEBUTTONUP:
        # pg.MOUSEBUTTONDOWN:
    }
