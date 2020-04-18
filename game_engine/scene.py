from game_engine.component.hitbox_component import HitboxComponent
from game_engine.component.particle_emitter_component import ParticleEmitterComponent


class Scene(object):
    def __init__(self):
        self._actors = []

    def add_actor(self, actor):
        self._actors.append(actor)

    def actors(self):
        return self._actors

    def colliding_actors(self):
        actors = []
        actors.extend(self.__actors_with_hitbox())
        actors.extend(self.__particles_with_hitbox())
        return actors

    def __actors_with_hitbox(self):
        return list(filter(lambda a: a.components(by_class=HitboxComponent), self._actors))

    def __particles_with_hitbox(self):
        particles = []
        emitter_actors = list(filter(lambda a: a.components(by_class=ParticleEmitterComponent), self._actors))
        for actor in emitter_actors:
            particles.extend(list(filter(lambda p: p.components(by_class=HitboxComponent), actor.components(by_class=ParticleEmitterComponent)[0].particles_alive)))
        return particles
