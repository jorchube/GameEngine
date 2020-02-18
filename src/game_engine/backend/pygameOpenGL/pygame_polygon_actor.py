from src.game_engine.backend.OpenGLWrapper import opengl


class PygamePolygonActor(object):
    def __init__(self, polygon_actor):
        self._actor = polygon_actor

    def draw(self):
        opengl.push_matrix()
        opengl.gl_translate_f(self._actor.position)
        opengl.draw_polygon(self._actor.points)
        opengl.pop_matrix()
