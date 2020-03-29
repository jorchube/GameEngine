from src.game_engine.component.component import Component


class ColorComponent(Component):
    def __init__(self, rgb):
        super().__init__()
        self.__rgb = rgb

    @property
    def rgb(self):
        return self.__rgb

    def update_rotation(self):
        pass

    def end_tick(self):
        pass
