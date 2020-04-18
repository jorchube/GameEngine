import unittest

from game_engine.actor.actor import Actor
from game_engine.actor.particle import Particle
from game_engine.display.display_configuration import DisplayConfiguration
from game_engine.game import Game
from game_engine.component.particle_emitter_component import ParticleEmitterComponent
from game_engine.geometry.vector import Vector3D


class TestParticleEmitter(unittest.TestCase):
    def setUp(self):
        self.fps = 60
        Game.set_display_configuration(DisplayConfiguration(800, 600, fps=self.fps))
        self.an_actor = Actor()
        self.test_emitter = ParticleEmitterComponent(OneSecondLifespanParticle, emission_rate=1, emission_vector=Vector3D(1, 0, 0))
        self.an_actor.add_component(self.test_emitter)

    def tearDown(self):
        pass

    def test_emitting_from_one_particle_descriptor(self):
        self.__elapse_one_second(self.test_emitter)

        assert 1 == self.test_emitter.particles_alive[0].end_tick_calls

    def test_discarding_particle_after_lifespan_is_exhausted(self):
        self.__elapse_one_second(self.test_emitter)
        assert 1 == len(self.test_emitter.particles_alive)

        self.test_emitter.emission_rate = 0.1
        self.__elapse_one_second(self.test_emitter)

        assert 0 == len(self.test_emitter.particles_alive)

    def test_emitting_particles_with_rate_one_per_second(self):
        self.__elapse_one_second(self.test_emitter)
        self.__elapse_one_second(self.test_emitter)
        self.__elapse_one_second(self.test_emitter)

        assert 1 == len(self.test_emitter.particles_alive)

    def test_emitting_particles_with_rate_two_per_second(self):
        self.test_emitter.emission_rate = 2

        self.__elapse_one_second(self.test_emitter)
        self.__elapse_ticks(self.test_emitter, 1)

        assert 2 == len(self.test_emitter.particles_alive)

    def test_emitting_particles_with_rate_half_per_second(self):
        self.test_emitter.emission_rate = 0.5

        self.__elapse_one_second(self.test_emitter)
        self.__elapse_one_second(self.test_emitter)
        self.__elapse_one_second(self.test_emitter)

        assert 1 == len(self.test_emitter.particles_alive)

    def __elapse_one_second(self, emitter):
        self.__elapse_ticks(emitter, self.fps)

    def __elapse_ticks(self, emitter, num_ticks):
        for _ in range(0, num_ticks):
            emitter.end_tick()


class OneSecondLifespanParticle(Particle):
    def __init__(self):
        super().__init__(1)
        self.end_tick_calls = 0

    def end_tick(self):
        super().end_tick()
        self.end_tick_calls += 1
