import unittest

from src.game_engine.actor.particle import ParticleDescriptor, Particle
from src.game_engine.display_configuration import DisplayConfiguration
from src.game_engine.game import Game
from src.game_engine.component.particle_emitter_component import ParticleEmitterComponent
from src.game_engine.geometry.vector import Vector3D


class TestParticleEmitter(unittest.TestCase):
    def setUp(self):
        self.fps = 60
        Game.set_display_configuration(DisplayConfiguration(800, 600, fps=self.fps))
        DummyParticleConstructor.particles_created = []
        self.particle_descriptor_1_second_lifespan = ParticleDescriptor(1, 1, 'a_polygon', 'a_rgb')
        self.particle_descriptor_999_second_lifespan = ParticleDescriptor(999, 999, 'a_polygon', 'a_rgb')

    def tearDown(self):
        pass

    def test_emitting_from_one_particle_descriptor(self):
        emitter = ParticleEmitterComponent(DummyParticleConstructor, [self.particle_descriptor_1_second_lifespan], 1, Vector3D(1, 0, 0))

        self.__elapse_one_second(emitter)

        assert 1 == DummyParticleConstructor.particles_created[0].end_tick_calls

    def test_discarding_particle_after_lifespan_is_exhausted(self):
        emitter = ParticleEmitterComponent(DummyParticleConstructor, [self.particle_descriptor_1_second_lifespan], 1, Vector3D(1, 0, 0))

        self.__elapse_one_second(emitter)
        self.__elapse_one_second(emitter)
        self.__elapse_one_second(emitter)

        assert self.fps == DummyParticleConstructor.particles_created[0].end_tick_calls

    def test_emitting_particles_with_rate_one_per_second(self):
        emitter = ParticleEmitterComponent(DummyParticleConstructor, [self.particle_descriptor_999_second_lifespan],
                                           emission_rate=1, emission_vector=Vector3D(1, 0, 0))

        self.__elapse_one_second(emitter)
        self.__elapse_one_second(emitter)

        assert 2 == len(DummyParticleConstructor.particles_created)

    def test_emitting_particles_with_rate_two_per_second(self):
        emitter = ParticleEmitterComponent(DummyParticleConstructor, [self.particle_descriptor_999_second_lifespan],
                                           emission_rate=2, emission_vector=Vector3D(1, 0, 0))

        self.__elapse_one_second(emitter)
        self.__elapse_one_second(emitter)
        emitter.end_tick()

        assert 4 == len(DummyParticleConstructor.particles_created)

    def test_emitting_particles_with_rate_half_per_second(self):
        emitter = ParticleEmitterComponent(DummyParticleConstructor, [self.particle_descriptor_999_second_lifespan],
                                           emission_rate=0.5, emission_vector=Vector3D(1, 0, 0))

        self.__elapse_one_second(emitter)
        self.__elapse_one_second(emitter)
        self.__elapse_one_second(emitter)

        assert 1 == len(DummyParticleConstructor.particles_created)

    def __elapse_one_second(self, emitter):
        for _ in range(0, self.fps):
            emitter.end_tick()


class DummyParticle(Particle):
    def __init__(self, lifespan_seconds):
        super().__init__(lifespan_seconds)
        self.end_tick_calls = 0

    def end_tick(self):
        super()._update_lifespan()
        self.end_tick_calls += 1


class DummyParticleConstructor(object):
    particles_created = []

    @classmethod
    def construct(cls, particle_descriptor):
        part = DummyParticle(particle_descriptor.max_lifespan_seconds)
        cls.particles_created.append(part)
        return part
