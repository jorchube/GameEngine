from game_engine.text.text_delegate import TextDelegateInterface
from pygame import font
from pygame import image
from game_engine.backend.OpenGLWrapper import opengl


class PygameTextDelegate(TextDelegateInterface):
    def __init__(self):
        if font.get_init() is None:
            font.init()

    def new_text(self, string, font_size, fg_color, bg_color):
        try:
            f = font.SysFont(None, font_size)
            text = f.render(string, False, fg_color, bg_color)
            return text
        except Exception as exc:
            print('Unable to create new text: {msg}'.format(msg=exc))

    def draw_text(self, a_text, position=None):
        text_data = image.tostring(a_text, "RGBA", True)
        opengl.gl_raster_position(position.x, position.y, position.z)
        opengl.gl_draw_pixels(text_data, a_text.get_width(), a_text.get_height())

