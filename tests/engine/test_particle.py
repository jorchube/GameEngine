import unittest
from unittest import mock

from game_engine.actor.particle import Particle
from game_engine.display.display_configuration import DisplayConfiguration
from game_engine.event.event_dispatcher import EventDispatcher
from game_engine.game import Game


class TestParticle(unittest.TestCase):
    def setUp(self):
        Game.set_display_configuration(DisplayConfiguration(800, 600, 1))
        EventDispatcher.append_event = mock.MagicMock()

    def test_emits_particle_expired_event_when_particle_expires(self):
        a_particle = Particle(1)

        a_particle.end_tick()

        EventDispatcher.append_event.assert_called_once()
