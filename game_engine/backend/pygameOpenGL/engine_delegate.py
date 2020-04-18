from game_engine.backend.OpenGLWrapper import opengl
from game_engine.backend.pygameOpenGL.pygame_to_event_converter import PygameToEventConverter

import pygame as pg
from pygame.locals import *
from game_engine.engine.engine_delegate import EngineDelegate


class PygameEngineDelegate(EngineDelegate):
    def __init__(self):
        self.__check_requirements()
        self.clock = None
        self.engine = None

    def initialize(self, engine, camera):
        self.clock = pg.time.Clock()
        self.engine = engine
        pg.init()
        pg.display.set_mode((engine.display_configuration.width, engine.display_configuration.height), self.__get_display_flags())
        opengl.glu_perspective(camera.fov, (engine.display_configuration.width / engine.display_configuration.height), camera.near_clipping_distance, camera.far_clipping_distance)
        opengl.gl_translate_f(camera.position)
        opengl.gl_rotate_f(camera.rotation.x_axis, camera.rotation.y_axis, camera.rotation.z_axis)

    def digest_events(self):
        events = filter(lambda event: PygameToEventConverter.can_convert_event(event.type), pg.event.get())
        self.engine.set_digested_events([PygameToEventConverter.convert(event) for event in events])

    def clear_display(self):
        opengl.clear_screen()

    def end_tick(self):
        pg.display.flip()
        self.clock.tick(self.engine.display_configuration.fps)

    def __get_display_flags(self):
        if self.engine.display_configuration.scaled:
            return DOUBLEBUF | OPENGL | SCALED
        return DOUBLEBUF | OPENGL

    def __check_requirements(self):
        if not opengl.check_requirements():
            print('')
            print('FATAL:')
            print('It seems that GLU libraries are not available on this system.')
            print('You can fix this by installing any GLU implementation.')
            exit(-1)
