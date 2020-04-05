import random

from src.game_engine.component.component import Component
from src.game_engine.game import Game
from src.game_engine.geometry.operations import GeometryOperations
from src.game_engine.geometry.vector import Vector3D


class ParticleEmitterComponent(Component):
    def __init__(self, particle_constructor, particle_descriptor_list, emission_rate, emission_vector, speed_variability=0, direction_variability=0):
        super().__init__()
        self.particle_constructor = particle_constructor
        self.particle_descriptors = particle_descriptor_list
        self.emission_rate = emission_rate
        self.emission_vector = emission_vector
        self.original_emission_vector = emission_vector
        self.speed_variability = speed_variability
        self.direction_variability = direction_variability
        self.particles_alive = []
        self.partial_particle_construction = 0

    def update_rotation(self):
        super().update_rotation()
        self.emission_vector = GeometryOperations.rotate_vector(self.original_emission_vector, self.actor.rotation.z_axis)

    def end_tick(self):
        self.__discard_exhausted_particles()
        self.__update_particles()
        for particle in self.particles_alive:
            particle.end_tick()

    def __discard_exhausted_particles(self):
        self.particles_alive = list(filter(lambda p: p.remaining_lifespan_seconds > 0, self.particles_alive))

    def __update_particles(self):
        self.partial_particle_construction += (1/Game.display_configuration().fps) * self.emission_rate
        while self.partial_particle_construction >= 1:
            self.particles_alive.append(self.__construct_particle())
            self.partial_particle_construction -= 1

    def __construct_particle(self):
        particle = self.particle_constructor.construct(self.particle_descriptors[0])
        particle.position = self.actor.position + self.position_offset_relative_to_actor
        self.__apply_emission_vector(particle)
        return particle

    def __apply_emission_vector(self, particle):
        particle.move_vector = Vector3D.multiply_vector_by_number(
            GeometryOperations.rotate_vector(self.emission_vector, self.__direction_variability()),
            self.__speed_variability()
        )

    def __direction_variability(self):
        return random.uniform(-(self.direction_variability / 2), (self.direction_variability / 2))

    def __speed_variability(self):
        return 1 - random.uniform(-(self.speed_variability / 2), (self.speed_variability / 2))