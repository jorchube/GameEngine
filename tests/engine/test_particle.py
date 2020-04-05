import unittest

from src.game_engine.actor.particle import Particle
from src.game_engine.display_configuration import DisplayConfiguration
from src.game_engine.game import Game


class TestParticle(unittest.TestCase):
    def setUp(self):
        Game.set_display_configuration(DisplayConfiguration(800, 600, 60))

    def test_particle_lifespan_decreasing_each_tick(self):
        a_particle = Particle(1)

        a_particle.end_tick()

        assert a_particle.remaining_lifespan_seconds < 1

