from game_engine.event import event


class ParticleExpiredEvent(event.Event):
    def __init__(self, particle):
        self.__particle = particle

    @property
    def particle(self):
        return self.__particle

