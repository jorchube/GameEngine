import unittest
from unittest import mock
from tests.helper import patcher

from src.game_engine.backend.pygameOpenGL.polygon_component_draw_delegate import PolygonComponentDrawDelegate


class TestPolygonComponentDrawDelegate(unittest.TestCase):
    def setUp(self):
        patcher.start_patch(self, 'src.game_engine.backend.OpenGLWrapper.opengl.push_matrix')
        patcher.start_patch(self, 'src.game_engine.backend.OpenGLWrapper.opengl.gl_translate_f')
        patcher.start_patch(self, 'src.game_engine.backend.OpenGLWrapper.opengl.draw_polygon')
        patcher.start_patch(self, 'src.game_engine.backend.OpenGLWrapper.opengl.pop_matrix')
        self.component = mock.MagicMock()
        self.component.position = mock.MagicMock()
        self.component.polygon = mock.MagicMock()

    def tearDown(self):
        patcher.stop_patches()

    def test_drawing_actor(self):
        delegate = PolygonComponentDrawDelegate()

        delegate.draw(self.component.polygon, self.component.position)

        self.push_matrix.assert_called_once()
        self.gl_translate_f.assert_called_once_with(self.component.position)
        self.draw_polygon.assert_called_once_with(self.component.polygon)
        self.pop_matrix.assert_called_once()



