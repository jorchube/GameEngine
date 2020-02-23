from src.game_engine.event.event_type.collision_event import CollisionEvent
from shapely.geometry import Polygon as sPol

from src.game_engine.geometry.point import Point3D


class CollisionEngine(object):
    def calculate_collisions(self, actors):
        actors_copy = actors.copy()
        while actors_copy:
            actor = actors_copy.pop()
            for other in actors_copy:
                if self.__actors_collide(actor, other):
                    self.__notify_collision(actor, other)
                    self.__notify_collision(other, actor)

    def __actors_collide(self, actor1, actor2):
        geometry1 = self.__geometry_from_actor(actor1)
        geometry2 = self.__geometry_from_actor(actor2)
        return sPol(geometry1).intersects(sPol(geometry2))

    def __notify_collision(self, actor1, actor2):
        actor1.receive_event(CollisionEvent(actor2))

    def __geometry_from_actor(self, actor):
        return [self.__normalize_with_position(point, actor.position).as_tuple() for point in actor.hitbox.point_list]

    def __normalize_with_position(self, point, position):
        return Point3D(point.x + position.x, point.y + position.y, point.z + position.z)
