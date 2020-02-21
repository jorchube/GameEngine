from src.game_engine.backend.OpenGLWrapper import opengl


class PolygonActorDrawDelegate(object):
    def draw(self, actor):
        opengl.push_matrix()
        opengl.gl_translate_f(actor.position)
        opengl.draw_polygon(actor.points)
        opengl.pop_matrix()
