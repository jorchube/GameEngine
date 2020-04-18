from game_engine.display.display import Display


class Text(object):
    class AText(object):
        __size = None
        __string = None
        __fg_color = None
        __bg_color = None
        __backend_data = None

        def __init__(self, string, size, fg_color, bg_color, delegate):
            self.__text_delegate = delegate
            self.__size = size if Display.configuration().scaled is False else size * 2
            self.__string = string
            self.__fg_color = self.__color_to_tuple(fg_color) if fg_color else (255, 255, 255, 255)
            self.__bg_color = self.__color_to_tuple(bg_color) if bg_color else (0, 0, 0, 255)
            self.__generate_text()

        def draw(self, position):
            self.__text_delegate.draw_text(self.__backend_data, position)

        def set_fg_color(self, color):
            self.__fg_color = self.__color_to_tuple(color) if color else (255, 255, 255, 255)
            self.__generate_text()

        def set_bg_color(self, color):
            self.__bg_color = self.__color_to_tuple(color) if color else (255, 255, 255, 255)
            self.__generate_text()

        def set_string(self, string):
            self.__string = string
            self.__generate_text()

        def set_size(self, size):
            self.__size = size if Display.configuration().scaled is False else size * 2
            self.__generate_text()

        def __generate_text(self):
            self.__backend_data = self.__text_delegate.new_text(self.__string, self.__size, self.__fg_color, self.__bg_color)

        def __color_to_tuple(self, color):
            return (int(color.red * 255), int(color.green * 255), int(color.blue * 255), 255)

    __text_delegate = None

    @classmethod
    def initialize(cls, text_delegate):
        cls.__text_delegate = text_delegate

    @classmethod
    def new_text(cls, string, size, fg_color, bg_color):
        return cls.AText(string, size, fg_color, bg_color, cls.__text_delegate)


