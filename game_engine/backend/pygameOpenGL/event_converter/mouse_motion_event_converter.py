from game_engine.backend.pygameOpenGL.event_converter.event_converter import EventConverter
from game_engine.event.event_type import mouse_motion_event


class MouseMotionEventConverter(EventConverter):
    @classmethod
    def convert(cls, event):
        return mouse_motion_event.MouseMotionEvent(event.pos[0], (-1) * event.pos[1])
