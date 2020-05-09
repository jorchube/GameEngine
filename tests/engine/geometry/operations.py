import unittest

from game_engine.geometry import Point3D, Polygon, GeometryOperations


class TestGeometryOperations(unittest.TestCase):
    def test_point_is_inside_polygon(self):
        point = Point3D(1, 1, 0)
        polygon = Polygon([Point3D(0, 0, 0), Point3D(2, 0, 0), Point3D(2, 2, 0), Point3D(0, 2, 0)])

        assert GeometryOperations.is_point_inside_polygon(point, polygon)

    def test_point_is_not_inside_polygon(self):
        point = Point3D(7, 7, 0)
        polygon = Polygon([Point3D(0, 0, 0), Point3D(2, 0, 0), Point3D(2, 2, 0), Point3D(0, 2, 0)])

        assert not GeometryOperations.is_point_inside_polygon(point, polygon)
