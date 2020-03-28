from src.game_engine.event import event


class Key(object):
    UP_ARROW = 'up'
    DOWN_ARROW = 'down'
    LEFT_ARROW = 'left'
    RIGHT_ARROW = 'right'
    W = 'w'
    A = 'a'
    S = 's'
    D = 'd'


class KeyEvent(event.Event):
    def __init__(self, key=None):
        self._key = key

    @property
    def key(self):
        return self._key

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.key == other.key


class KeyEventPress(KeyEvent):
    pass


class KeyEventRelease(KeyEvent):
    pass
