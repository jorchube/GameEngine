class Scene(object):
    def __init__(self):
        self._actors = []

    def add_actor(self, actor):
        self._actors.append(actor)

    def actors(self):
        return self._actors
