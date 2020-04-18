import unittest
from unittest import mock

from game_engine.audio.audio import Audio


class TestAudio(unittest.TestCase):
    def setUp(self):
        self.audio_delegate = mock.MagicMock()
        Audio.initialize(self.audio_delegate)

    def test_should_create_and_play_a_sound(self):
        self.audio_delegate.new_sound.return_value = 'new_sound'

        sound = Audio.new_sound('/some/audio/file/path.wav')
        sound.play()

        self.audio_delegate.new_sound.assert_called_with('/some/audio/file/path.wav')
        self.audio_delegate.play_sound.assert_called_with('new_sound')



