class Component(object):
    def __init__(self):
        self.__actor = None
        self.__tag = None

    @property
    def actor(self):
        return self.__actor

    @actor.setter
    def actor(self, actor):
        self.__actor = actor

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def tag(self, tag):
        self.__tag = tag

    @property
    def position(self):
        return self.actor.position

    def update_rotation(self):
        raise NotImplementedError

    def end_tick(self):
        raise NotImplementedError

    def __eq__(self, other):
        return self == other

    def __ne__(self, other):
        return not self.__eq__(other)
