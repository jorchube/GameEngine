import unittest

from src.game_engine.geometry.point import Point3D
from src.game_engine.geometry.polygon import Polygon
from src.game_engine.geometry.polygon import PolygonConstructionError


class TestPolygon(unittest.TestCase):
    def test_creating_a_polygon(self):
        point_list = [Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(2, 2, 2)]

        polygon = Polygon(point_list)

        assert polygon.point_list == point_list

    def test_raising_exception_when_constructing_a_polygon_with_insufficient_points(self):
        self.assertRaises(PolygonConstructionError, Polygon, [Point3D(0, 0, 0), Point3D(1, 1, 1)])