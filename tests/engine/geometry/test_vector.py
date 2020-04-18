import unittest

from game_engine.geometry.vector import Vector3D
from game_engine.geometry.point import Point3D


class TestVector3D(unittest.TestCase):
    def test_creating_a_3d_vector(self):
        vector = Vector3D(1, 2, 3)

        assert vector.x == 1
        assert vector.y == 2
        assert vector.z == 3

    def test_creating_a_3d_vector_setting_an_origin_point(self):
        vector = Vector3D(5, 6, 7, origin=Point3D(1, 3, 5))

        assert vector.x == 4
        assert vector.y == 3
        assert vector.z == 2

    def test_adding_two_vectors(self):
        added = Vector3D(1, 2, 3) + Vector3D(3, 4, 5)

        assert added.x == 4
        assert added.y == 6
        assert added.z == 8

    def test_substracting_two_vectors(self):
        added = Vector3D(5, 2, 17) - Vector3D(3, 4, 5)

        assert added.x == 2
        assert added.y == -2
        assert added.z == 12

    def test_comparing_two_vectors(self):
        assert Vector3D(1, 2, 3) == Vector3D(1, 2, 5, origin=Point3D(0, 0, 2))
        assert Vector3D(1, 2, 3) != Vector3D(1, 2, 5)

    def test_dividing_by_number(self):
        p1 = Vector3D(1, 2, 3)

        assert Vector3D(0.5, 1, 1.5) == Vector3D.divide_vector_by_number(p1, 2)

    def test_multiplying_by_number(self):
        p1 = Vector3D(1, 2, 3)

        assert Vector3D(2, 4, 6) == Vector3D.multiply_vector_by_number(p1, 2)