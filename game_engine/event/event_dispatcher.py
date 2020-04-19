class EventDispatcher(object):
    __event_list = []

    @classmethod
    def append_event(cls, event):
        cls.__event_list.append(event)

    @classmethod
    def append_event_list(cls, event_list):
        cls.__event_list.extend(event_list)

    @classmethod
    def dispatch_events(cls):
        from game_engine.game import Game
        while cls.__event_list:
            event = cls.__event_list.pop()
            Game.receive_event(event)
            cls.__forward_event_to_actors(event)

    @classmethod
    def __forward_event_to_actors(cls, event):
        from game_engine.game import Game
        for actor in Game.current_scene().actors():
            actor.receive_event(event)

