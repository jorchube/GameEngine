from game_engine.component.hitbox_component import HitboxComponent
from game_engine.event import event_handler
from game_engine.event.event_type.particle_expired_event import ParticleExpiredEvent


class Scene(object):
    def __init__(self, display):
        self.__event_handler = event_handler.EventHandler()
        self._actors = []
        self.subscribe_to_event(ParticleExpiredEvent, self.__on_particle_expired_event)

    def subscribe_to_event(self, event_type, callback):
        self.__event_handler.subscribe(event_type, callback)

    def receive_event(self, event):
        if not self.__event_handler.event(event):
            self.__forward_event_to_actors(event)

    def __forward_event_to_actors(self, event):
        for actor in self._actors:
            actor.receive_event(event)

    def add_actor(self, actor):
        self._actors.append(actor)

    def remove_actor(self, actor):
        if actor in self._actors:
            self._actors.remove(actor)

    def actors(self):
        return self._actors

    def colliding_actors(self):
        actors = []
        actors.extend(self.__actors_with_hitbox(self._actors))
        return actors

    def end_tick(self):
        self.__notify_end_tick_to_actors(self._actors)

    def __notify_end_tick_to_actors(self, actor_list):
        for actor in actor_list:
            actor.end_tick()

    def draw(self):
        for actor in self._actors:
            actor.draw()

    def __actors_with_hitbox(self, actor_list):
        return list(filter(lambda a: a.components(by_class=HitboxComponent), actor_list))

    def __on_particle_expired_event(self, event):
        self.remove_actor(event.particle)
