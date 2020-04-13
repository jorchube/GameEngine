import unittest
from unittest import mock

from src.game_engine.text.text import Text
from src.game_engine.visual.rgb import RGB


class TestText(unittest.TestCase):
    def setUp(self):
        self.text_delegate = mock.MagicMock()
        Text.initialize(self.text_delegate)

    def test_should_create_and_draw_a_text(self):
        self.text_delegate.new_text.return_value = 'new_text'
        fg = RGB(0, 0.5, 1)
        bg = RGB(1, 0, 0)

        a_text = Text.new_text('a_string', 33, fg, bg)
        a_text.draw('a_position')

        self.text_delegate.new_text.assert_called_with('a_string', 33, (0, 127, 255, 255), (255, 0, 0, 255))
        self.text_delegate.draw_text.assert_called_with('new_text', 'a_position')



