import random

from src.game_engine.component.component import Component
from src.game_engine.geometry.operations import GeometryOperations
from src.game_engine.geometry.vector import Vector3D


class ParticleEmitterComponent(Component):
    def __init__(self, particle_class, emission_rate, emission_vector, speed_variability=0, direction_variability=0):
        super().__init__()
        self.__particle_class = particle_class
        self.__emission_rate = emission_rate
        self.__emission_vector = emission_vector
        self.__original_emission_vector = emission_vector
        self.__speed_variability = speed_variability
        self.__direction_variability = direction_variability
        self.__partial_particle_construction = 0
        self.__particles_alive = []

    @property
    def particles_alive(self):
        return self.__particles_alive

    @property
    def emission_rate(self):
        return self.__emission_rate

    @emission_rate.setter
    def emission_rate(self, rate):
        self.__emission_rate = rate

    @property
    def speed_variability(self):
        return self.__speed_variability

    @speed_variability.setter
    def speed_variability(self, variability):
        self.__speed_variability = variability

    @property
    def direction_variability(self):
        return self.__direction_variability

    @direction_variability.setter
    def direction_variability(self, variability):
        self.__direction_variability = variability

    def update_rotation(self):
        super().update_rotation()
        self.__emission_vector = GeometryOperations.rotate_vector(self.__original_emission_vector, self.actor.rotation.z_axis)

    def end_tick(self):
        self.__discard_exhausted_particles()
        self.__update_particles()
        for particle in self.__particles_alive:
            particle.end_tick()

    def __discard_exhausted_particles(self):
        self.__particles_alive = list(filter(lambda p: p.remaining_lifespan_seconds > 0, self.__particles_alive))

    def __update_particles(self):
        from src.game_engine.game import Game
        self.__partial_particle_construction += (1 / Game.display_configuration().fps) * self.__emission_rate
        while self.__partial_particle_construction >= 1:
            self.__particles_alive.append(self.__construct_particle())
            self.__partial_particle_construction -= 1

    def __construct_particle(self):
        particle = self.__particle_class()
        particle.position = self.actor.position + self.position_offset_relative_to_actor
        self.__apply_emission_vector(particle)
        return particle

    def __apply_emission_vector(self, particle):
        particle.move_vector = Vector3D.multiply_vector_by_number(
            GeometryOperations.rotate_vector(self.__emission_vector, self.__calculate_direction_variability()),
            self.__calculate_speed_variability()
        )

    def __calculate_direction_variability(self):
        return random.uniform(-(self.__direction_variability / 2), (self.__direction_variability / 2))

    def __calculate_speed_variability(self):
        return 1 - random.uniform(-(self.__speed_variability / 2), (self.__speed_variability / 2))