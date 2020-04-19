from game_engine.actor.actor import Actor
from game_engine.event.event_dispatcher import EventDispatcher
from game_engine.event.event_type.particle_expired_event import ParticleExpiredEvent
from game_engine.game import Game


class Particle(Actor):
    def __init__(self, lifespan_seconds):
        super().__init__()
        self.__remaining_lifespan = lifespan_seconds

    @property
    def remaining_lifespan_seconds(self):
        return self.__remaining_lifespan

    def end_tick(self):
        self._update_lifespan()
        super().end_tick()

    def _update_lifespan(self):
        self.__remaining_lifespan -= 1/Game.display_configuration().fps
        if self.__remaining_lifespan <= 0:
            EventDispatcher.append_event(ParticleExpiredEvent(self))

