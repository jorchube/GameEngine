from game_engine.backend.pygameOpenGL.event_converter.event_converter import EventConverter
from game_engine.event.event_type.quit_event import QuitEvent


class QuitEventConverter(EventConverter):
    @classmethod
    def convert(cls, event):
        return QuitEvent()
