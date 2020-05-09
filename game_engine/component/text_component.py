from game_engine.component.component import Component
from game_engine.text.text import Text


class TextComponent(Component):
    def __init__(self, a_string, size=12, fg_color=None, bg_color=None):
        super().__init__()
        self.__text = Text.new_text(a_string, size, fg_color, bg_color)

    @property
    def text(self):
        return self.__text

    def end_tick(self):
        pass

    def draw(self):
        self.__text.draw(self.actor.position)
