from src.game_engine import engine
from src.game_engine.geometry.point import Point3D
from src.game_engine.backend.OpenGLWrapper import opengl
from src.game_engine.backend.pygameOpenGL import pygame_polygon_actor
from src.game_engine.backend.pygameOpenGL.pygame_to_event_converter import PygameToEventConverter

import pygame as pg
from pygame.locals import *



class PygameEngine(engine.Engine):
    def __init__(self, framerate, display_configuration, initial_scene):
        super(PygameEngine, self).__init__(framerate, display_configuration, initial_scene)
        self.clock = pg.time.Clock()
        self.fps = framerate
        self.display = (display_configuration.width, display_configuration.height)
        pg.init()
        pg.display.set_mode(self.display, DOUBLEBUF|OPENGL)
        opengl.glu_perspective(45, (self.display[0] / self.display[1]), 0.1, 100.0)  # FIXME: This belongs to a scene/camera module
        opengl.gl_translate_f(Point3D(0, 0, -50))  # FIXME: This belongs to a scene/camera module

    def _draw_actors(self, actors):
        for actor in actors:
            pygame_polygon_actor.PygamePolygonActor(actor).draw()

    def _end_tick(self):
        self.clock.tick(self.fps)
        opengl.clear_screen()
        self._draw_actors(self._scene.actors())
        pg.display.flip()

    def _process_events(self):
        for event in pg.event.get():
            if PygameToEventConverter.can_convert_event(event.type):
                self._forward_event_to_actors(PygameToEventConverter.convert(event))

    def _forward_event_to_actors(self, event):
        for actor in self._scene.actors():
            actor.receive_event(event)


