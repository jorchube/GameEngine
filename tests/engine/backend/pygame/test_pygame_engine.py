import unittest
from unittest import mock

from tests.helper import patcher

from src.game_engine.event.event_type import key_event
from src.game_engine.display_configuration import DisplayConfiguration
from src.game_engine.backend.pygameOpenGL.pygame_engine import PygameEngine

from pygame.locals import *
import pygame as pg


class TestPygameBackendEngine(unittest.TestCase):
    def setUp(self):
        patcher.start_patch(self, 'pygame.init')
        patcher.start_patch(self, 'pygame.time')
        patcher.start_patch(self, 'pygame.event.get')
        self.pygame_clock = mock.MagicMock()
        self.time.Clock.return_value = self.pygame_clock
        patcher.start_patch(self, 'pygame.display.set_mode')
        patcher.start_patch(self, 'pygame.display.flip')
        patcher.start_patch(self, 'src.game_engine.backend.pygameOpenGL.pygame_polygon_actor.PygamePolygonActor')
        patcher.start_patch(self, 'src.game_engine.backend.OpenGLWrapper.opengl.clear_screen')
        patcher.start_patch(self, 'src.game_engine.backend.OpenGLWrapper.opengl.gl_translate_f')
        patcher.start_patch(self, 'src.game_engine.backend.OpenGLWrapper.opengl.glu_perspective')
        self.test_scene = mock.MagicMock()
        self.pygame_actor = mock.MagicMock()
        self.PygamePolygonActor.return_value = self.pygame_actor
        self.test_scene.actors.return_value = [self.pygame_actor]

    def tearDown(self):
        patcher.stop_patches()

    def test_should_create_engine(self):
        PygameEngine(60, DisplayConfiguration(800, 600), self.test_scene)

        self.time.Clock.assert_called_once()
        self.init.assert_called_once()
        self.set_mode.assert_called_once_with((800, 600), DOUBLEBUF|OPENGL)

    def test_should_redraw_display_and_sync_to_framerate_on_tick_end(self):
        engine = PygameEngine(60, DisplayConfiguration(800, 600), self.test_scene)

        engine._end_tick()

        self.pygame_clock.tick.assert_called_with(60)
        self.flip.assert_called_once()

    def test_should_create_pygame_actors_and_draw_them_on_draw_actors_call(self):
        actor = mock.MagicMock()
        engine = PygameEngine(60, DisplayConfiguration(800, 600), self.test_scene)

        engine._draw_actors([actor])

        self.PygamePolygonActor.assert_called_once_with(actor)
        self.pygame_actor.draw.assert_called_once()

    def test_should_forward_processed_key_event_to_actors(self):
        an_event = PygameKeyEventTest()
        self.get.return_value = [an_event]
        engine = PygameEngine(60, DisplayConfiguration(800, 600), self.test_scene)

        engine._process_events()

        self.pygame_actor.receive_event.assert_called_once_with(key_event.KeyEventPress(key_event.Key.RIGHT_ARROW))


class PygameKeyEventTest(object):
    def __init__(self):
        self.type = pg.KEYDOWN
        self.key = pg.K_RIGHT
