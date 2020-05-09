from game_engine.component.component import Component


class ColorComponent(Component):
    def __init__(self, rgb):
        super().__init__()
        self.__rgb = rgb

    @property
    def rgb(self):
        return self.__rgb

    def end_tick(self):
        pass

    def draw(self):
        pass
