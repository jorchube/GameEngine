from src.game_engine.game import Game


class Text(object):
    class AText(object):
        __size = None
        __string = None
        __backend_data = None

        def __init__(self, string, size, delegate):
            self.__text_delegate = delegate
            self.set_size(size)
            self.set_string(string)
            self.__generate_text()

        def draw(self, position):
            self.__text_delegate.draw_text(self.__backend_data, position)

        def set_string(self, string):
            self.__string = string
            self.__generate_text()

        def set_size(self, size):
            self.__size = size if Game.display_configuration().scaled is False else size * 2
            self.__generate_text()

        def __generate_text(self):
            self.__backend_data = self.__text_delegate.new_text(self.__string, self.__size)

    __text_delegate = None

    @classmethod
    def initialize(cls, text_delegate):
        cls.__text_delegate = text_delegate

    @classmethod
    def new_text(cls, string, size):
        return cls.AText(string, size, cls.__text_delegate)


