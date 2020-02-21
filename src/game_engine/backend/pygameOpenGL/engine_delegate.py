from src.game_engine.geometry.point import Point3D
from src.game_engine.backend.OpenGLWrapper import opengl
from src.game_engine.backend.pygameOpenGL.pygame_to_event_converter import PygameToEventConverter

import pygame as pg
from pygame.locals import *
from src.game_engine.engine.engine_delegate import EngineDelegate


class PygameEngineDelegate(EngineDelegate):
    def __init__(self):
        self.clock = None
        self.framerate = None

    def initialize(self, engine):
        self.clock = pg.time.Clock()
        self.framerate = engine.framerate
        pg.init()
        pg.display.set_mode((engine.display.width, engine.display.height), DOUBLEBUF|OPENGL)
        opengl.glu_perspective(45, (engine.display.width/engine.display.height), 0.1, 100.0)  # FIXME: This belongs to a scene/camera module
        opengl.gl_translate_f(Point3D(0, 0, -50))  # FIXME: This belongs to a scene/camera module

    def digest_events(self, engine):
        events = filter(lambda event: PygameToEventConverter.can_convert_event(event.type), pg.event.get())
        engine.set_digested_events([PygameToEventConverter.convert(event) for event in events])

    def clear_display(self):
        opengl.clear_screen()

    def end_tick(self):
        pg.display.flip()
        self.clock.tick(self.framerate)
