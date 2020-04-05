from src.game_engine.actor.actor import Actor
from src.game_engine.game import Game


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
