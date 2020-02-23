from src.game_engine.event import event


class CollisionEvent(event.Event):
    def __init__(self, colliding_actor=None):
        self.__colliding_actor = colliding_actor

    @property
    def colliding_actor(self):
        return self.__colliding_actor

    def __eq__(self, other):
        return self.type == other.type and self.colliding_actor == other.colliding_actor

