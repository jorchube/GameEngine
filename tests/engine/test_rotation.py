import unittest
from unittest import mock

from src.game_engine.geometry.rotation import Rotation


class TestRotation(unittest.TestCase):
    def test_setting_and_getting_a_rotation_object_components(self):
        callback = mock.MagicMock()

        rotation = Rotation(rotation_callback=callback)

        rotation.x_axis = 30
        rotation.y_axis = 60
        rotation.z_axis = 90

        assert callback.call_count == 3
        assert rotation.x_axis == 30
        assert rotation.y_axis == 60
        assert rotation.z_axis == 90

        rotation.x_axis = 400
        rotation.y_axis = 405
        rotation.z_axis = 410

        assert callback.call_count == 6
        assert rotation.x_axis == 40
        assert rotation.y_axis == 45
        assert rotation.z_axis == 50

        rotation.x_axis = -350
        rotation.y_axis = -370
        rotation.z_axis = -360

        assert callback.call_count == 9
        assert rotation.x_axis == 10
        assert rotation.y_axis == 350
        assert rotation.z_axis == 0


