import unittest
from unittest import mock

from src.game_engine.collision_engine import CollisionEngine
from src.game_engine.event.event_type.collision_event import CollisionEvent
from src.game_engine.geometry.point import Point3D
from src.game_engine.geometry.polygon import Polygon


class TestCollisionEngine(unittest.TestCase):
    def setUp(self):
        self.actor1 = mock.MagicMock()
        self.actor2 = mock.MagicMock()
        self.actor3 = mock.MagicMock()
        self.actor4 = mock.MagicMock()
        self.actor1.hitbox = Polygon([Point3D(0, 0, 0), Point3D(1, 0, 0), Point3D(0, 1, 0)])
        self.actor2.hitbox = Polygon([Point3D(0, 0, 0), Point3D(1, 1, 0), Point3D(0, 1, 0)])
        self.actor3.hitbox = Polygon([Point3D(0, 0, 0), Point3D(1, 0, 0), Point3D(1, 1, 0), Point3D(0, 1, 0)])
        self.actor4.hitbox = Polygon([Point3D(0, 0, 0), Point3D(1, 0, 0), Point3D(1, 1, 0), Point3D(0, 1, 0)])
        self.actor1.position = Point3D(0, 0, 0)
        self.actor2.position = Point3D(0, 0, 0)
        self.actor3.position = Point3D(3, 3, 0)
        self.actor4.position = Point3D(2.5, 2.5, 0)
        self.collision_engine = CollisionEngine()

    def test_notifying_each_actor_involved_on_a_collision(self):
        self.collision_engine.calculate_collisions([self.actor1, self.actor2])

        self.actor1.receive_event.assert_called_with(CollisionEvent(self.actor2))
        self.actor2.receive_event.assert_called_with(CollisionEvent(self.actor1))

        self.collision_engine.calculate_collisions([self.actor3, self.actor4])

        self.actor3.receive_event.assert_called_with(CollisionEvent(self.actor4))
        self.actor4.receive_event.assert_called_with(CollisionEvent(self.actor3))

    def test_doing_nothing_when_actors_do_not_collide(self):
        self.collision_engine.calculate_collisions([self.actor1, self.actor3])

        self.actor1.receive_event.assert_not_called()
        self.actor3.receive_event.assert_not_called()



