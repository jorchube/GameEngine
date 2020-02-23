import unittest

from src.game_engine.actor.polygon_actor import PolygonActor
from src.game_engine.geometry.point import Point3D
from src.game_engine.geometry.polygon import Polygon


class TestPolygonActor(unittest.TestCase):
    def test_creating_a_polygon_actor_with_a_polygon(self):
        polygon = Polygon([Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(2, 2, 2)])

        an_actor = PolygonActor(polygon)

        assert an_actor

    def test_returning_hitbox_should_be_equal_to_point_list(self):
        polygon = Polygon([Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(2, 2, 2)])

        an_actor = PolygonActor(polygon)

        assert polygon == an_actor.hitbox