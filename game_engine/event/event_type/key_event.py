from game_engine.event import event


class Key(object):
    UP_ARROW = 'up'
    DOWN_ARROW = 'down'
    LEFT_ARROW = 'left'
    RIGHT_ARROW = 'right'
    W = 'w'
    A = 'a'
    S = 's'
    D = 'd'
    zero = '0'
    one = '1'
    two = '2'
    three = '3'
    four = '4'
    five = '5'
    six = '6'
    seven = '7'
    eight = '8'
    nine = '9'
    ctrl_left = 'ctrl_left'
    shift_left = 'shift_left'
    space = 'space'




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
