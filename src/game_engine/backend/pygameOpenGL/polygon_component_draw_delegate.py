from src.game_engine.component.polygon_component_draw_delegate import DrawPolygonComponentDelegate
from src.game_engine.backend.OpenGLWrapper import opengl


class PolygonComponentDrawDelegate(DrawPolygonComponentDelegate):
    def draw(self, polygon, position):
        opengl.push_matrix()
        opengl.gl_translate_f(position)
        opengl.draw_polygon(polygon)
        opengl.pop_matrix()


