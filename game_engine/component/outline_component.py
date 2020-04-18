from game_engine.component.component import Component


class OutlineComponent(Component):
    def __init__(self, rgb, thickness=1):
        super().__init__()
        self.__rgb = rgb
        self.__thickness = thickness

    @property
    def rgb(self):
        return self.__rgb

    @property
    def thickness(self):
        return self.__thickness

    def end_tick(self):
        pass
