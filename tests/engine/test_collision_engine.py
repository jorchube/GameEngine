import unittest

from src.game_engine.actor.actor import Actor
from src.game_engine.collision_engine import CollisionEngine
from src.game_engine.event.event_type import collision_event
from src.game_engine.geometry.point import Point3D
from src.game_engine.component.hitbox_component import HitboxComponent
from src.game_engine.geometry.polygon import Polygon


class TestCollisionEngine(unittest.TestCase):
    def setUp(self):
        self.actor1 = DummyActor()
        self.actor2 = DummyActor()
        self.actor3 = DummyActor()
        self.actor1.position = Point3D(0, 0, 0)
        self.actor2.position = Point3D(0.5, 0, 0)
        self.actor3.position = Point3D(3, 3, 0)

        component1 = HitboxComponent(Polygon([Point3D(0, 0, 0), Point3D(1, 0, 0), Point3D(0, 1, 0)]), is_collision_source=True)
        self.actor1.add_component(component1)

        component2 = HitboxComponent(Polygon([Point3D(0, 0, 0), Point3D(1, 1, 0), Point3D(0, 1, 0)]))
        self.actor2.add_component(component2)

        component3 = HitboxComponent(Polygon([Point3D(0, 0, 0), Point3D(1, 0, 0), Point3D(1, 1, 0), Point3D(0, 1, 0)]))
        self.actor3.add_component(component3)
        
        self.collision_engine = CollisionEngine()

    def test_notifying_each_actor_involved_on_a_collision(self):
        self.collision_engine.calculate_collisions([self.actor1, self.actor2])

        assert self.actor1.has_collided
        assert self.actor2.has_collided
        assert not self.actor3.has_collided

        assert self.actor1.colliding_actor == self.actor2
        assert self.actor2.colliding_actor == self.actor1

    def test_doing_nothing_when_actors_do_not_collide(self):
        self.collision_engine.calculate_collisions([self.actor1, self.actor3])

        assert not self.actor1.has_collided
        assert not self.actor3.has_collided


class DummyActor(Actor):
    def __init__(self):
        super().__init__()
        self.subscribe_to_event(collision_event.CollisionEvent, self.__on_collision_event)
        self.has_collided = False
        self.colliding_actor = None

    def __on_collision_event(self, event):
        self.has_collided = True
        self.colliding_actor = event.colliding_actor
