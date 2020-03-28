import unittest

from src.game_engine.geometry.point import Point3D


class TestPoint3D(unittest.TestCase):
    def test_should_create_3D_point(self):
        point = Point3D(x=2, y=4, z=6)

        assert 2 == point.x
        assert 4 == point.y
        assert 6 == point.z
        assert (2, 4, 6) == point.as_tuple()
        assert '(2,4,6)' == '{0}'.format(point)

    def test_comparing_two_points_return_true_when_are_equal(self):
        p1 = Point3D(1, 2, 3)
        p2 = Point3D(1, 2, 3)

        assert p1 == p2

    def test_comparing_two_points_return_false_when_are_not_equal(self):
        p1 = Point3D(1, 3, 0)
        p2 = Point3D(1, 2, 0)

        assert p1 != p2

    def test_setting_a_component(self):
        point = Point3D(0, 0, 0)

        point.x = 1
        point.y = 2
        point.z = 3

        assert (1, 2, 3) == point.as_tuple()

    def test_adding_two_points(self):
        p1 = Point3D(1, 2, 3)
        p2 = Point3D(1, 2, 3)

        assert Point3D(2, 4, 6) == p1 + p2

    def test_substracting_two_points(self):
        p1 = Point3D(3, 6, 9)
        p2 = Point3D(1, 2, 3)

        assert Point3D(2, 4, 6) == p1 - p2
