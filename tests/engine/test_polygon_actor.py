import unittest

from src.game_engine.actor.polygon_actor import PolygonActor
from src.game_engine.actor.polygon_actor import PolygonActorConstructionError
from src.game_engine.geometry.point import Point3D


class TestPolygonActor(unittest.TestCase):
    def test_should_create_a_polygon_actor_with_a_list_of_3D_points(self):
        point_list = [Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(2, 2, 2)]

        an_actor = PolygonActor(point_list)

        assert '{0}'.format(an_actor) == '{Polygon actor: (0,0,0) (1,1,1) (2,2,2)}'

    def test_should_raise_exception_when_constructing_a_polygon_actor_with_insufficient_points(self):
        self.assertRaises(PolygonActorConstructionError, PolygonActor, [Point3D(0, 0, 0), Point3D(1, 1, 1)])

