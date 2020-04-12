import unittest
from unittest import mock

from src.game_engine.text.text import Text


class TestText(unittest.TestCase):
    def setUp(self):
        self.text_delegate = mock.MagicMock()
        Text.initialize(self.text_delegate)

    def test_should_create_and_draw_a_text(self):
        self.text_delegate.new_text.return_value = 'new_text'

        a_text = Text.new_text('a_string', 33)
        a_text.draw('a_position')

        self.text_delegate.new_text.assert_called_with('a_string', 33)
        self.text_delegate.draw_text.assert_called_with('new_text', 'a_position')



