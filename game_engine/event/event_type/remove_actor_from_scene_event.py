from game_engine.event import event


class RemoveActorFromSceneEvent(event.Event):
    def __init__(self, actor):
        self.__actor = actor

    @property
    def actor(self):
        return self.__actor

