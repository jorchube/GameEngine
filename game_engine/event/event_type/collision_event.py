from game_engine.event import event


class CollisionEvent(event.Event):
    def __init__(self, colliding_actor=None):
        self.__colliding_actor = colliding_actor

    @property
    def colliding_actor(self):
        return self.__colliding_actor

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.colliding_actor == other.colliding_actor

