from game_engine.component.polygon_component_draw_delegate import DrawPolygonComponentDelegate
from game_engine.backend.OpenGLWrapper import opengl


class PolygonComponentDrawDelegate(DrawPolygonComponentDelegate):
    def draw(self, polygon, position, rgb_fill=None, rgb_outline=None, outline_thickness=None):
        opengl.push_matrix()
        opengl.gl_translate_f(position)
        opengl.draw_polygon(polygon, rgb_fill, rgb_outline, outline_thickness)
        opengl.pop_matrix()


