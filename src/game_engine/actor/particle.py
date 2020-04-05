import random

from src.game_engine.actor.actor import Actor
from src.game_engine.component.color_component import ColorComponent
from src.game_engine.component.hitbox_component import HitboxComponent
from src.game_engine.component.polygon_component import PolygonComponent
from src.game_engine.game import Game


class ParticleDescriptor(object):
    def __init__(self, max_lifespan_seconds, min_lifespan_seconds, polygon, rgb_color, spinning_speed=0):
        self.max_lifespan_seconds = max_lifespan_seconds
        self.min_lifespan_seconds = min_lifespan_seconds
        self.polygon = polygon
        self.rgb = rgb_color
        self.spinning_speed = spinning_speed


class ParticleConstructor(object):
    @classmethod
    def construct(cls, particle_descriptor):
        lifespan = random.uniform(particle_descriptor.min_lifespan_seconds, particle_descriptor.max_lifespan_seconds)
        polygon_component = PolygonComponent(particle_descriptor.polygon)
        color_component = ColorComponent(particle_descriptor.rgb)
        particle = Particle(lifespan)
        particle.spinning_speed = particle_descriptor.spinning_speed
        particle.add_component(polygon_component)
        particle.add_component(color_component)
        return particle


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
