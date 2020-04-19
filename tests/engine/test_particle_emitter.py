import unittest
from unittest import mock

from game_engine.actor.actor import Actor
from game_engine.actor.particle import Particle
from game_engine.display.display_configuration import DisplayConfiguration
from game_engine.game import Game
from game_engine.component.particle_emitter_component import ParticleEmitterComponent
from game_engine.geometry.vector import Vector3D


class TestParticleEmitter(unittest.TestCase):
    def setUp(self):
        self.fps = 60
        self.scene = mock.MagicMock()
        Game.set_display_configuration(DisplayConfiguration(800, 600, fps=self.fps))
        Game.set_scene(self.scene)
        self.game = Game
        self.an_actor = Actor()
        self.test_emitter = ParticleEmitterComponent(OneSecondLifespanParticle, emission_rate=1, emission_vector=Vector3D(1, 0, 0))
        self.an_actor.add_component(self.test_emitter)

    def tearDown(self):
        pass

    def test_emitting_from_one_particle_descriptor(self):
        self.__elapse_one_second(self.test_emitter)

        self.scene.add_actor.assert_called_once()

    def test_emitting_particles_with_rate_one_per_second(self):
        self.__elapse_one_second(self.test_emitter)
        self.__elapse_one_second(self.test_emitter)
        self.__elapse_one_second(self.test_emitter)

        assert 3 == self.scene.add_actor.call_count

    def test_emitting_particles_with_rate_two_per_second(self):
        self.test_emitter.emission_rate = 2

        self.__elapse_one_second(self.test_emitter)
        self.__elapse_ticks(self.test_emitter, 1)

        assert 2 == self.scene.add_actor.call_count

    def test_emitting_particles_with_rate_half_per_second(self):
        self.test_emitter.emission_rate = 0.5

        self.__elapse_one_second(self.test_emitter)
        self.__elapse_one_second(self.test_emitter)
        self.__elapse_one_second(self.test_emitter)

        assert 1 == self.scene.add_actor.call_count

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
