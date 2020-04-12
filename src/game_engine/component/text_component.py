from src.game_engine.component.component import Component
from src.game_engine.text.text import Text


class TextComponent(Component):
    def __init__(self, a_string, size=12):
        super().__init__()
        self.__text = Text.new_text(a_string, size)

    @property
    def text(self):
        return self.__text

    def end_tick(self):
        self.__text.draw(self.actor.position)
