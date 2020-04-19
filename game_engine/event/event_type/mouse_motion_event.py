from game_engine.event import event


class MouseMotionEvent(event.Event):
    def __init__(self, delta_x, delta_y):
        self.__delta_x = delta_x
        self.__delta_y = delta_y

    @property
    def delta_x(self):
        return self.__delta_x

    @property
    def delta_y(self):
        return self.__delta_y
