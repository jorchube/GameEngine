from src.game_engine.event.event_type.collision_event import CollisionEvent
from shapely.geometry import Polygon as sPol

class CollisionEngine(object):
    def calculate_collisions(self, actors):
        collider_actors = list(filter(lambda a: a.check_collisions, actors))
        while collider_actors:
            actor = collider_actors.pop()
            for other in actors:
                if actor is not other:
                    self.__notify_actors_if_collide(actor, other)

    def __notify_actors_if_collide(self, actor1, actor2):
        if self.__actors_collide(actor1, actor2):
            self.__notify_collision(actor1, actor2)
            self.__notify_collision(actor2, actor1)

    def __actors_collide(self, actor1, actor2):
        geometry1 = self.__geometry_from_actor(actor1)
        geometry2 = self.__geometry_from_actor(actor2)
        return sPol(geometry1).intersects(sPol(geometry2))

    def __notify_collision(self, actor1, actor2):
        actor1.receive_event(CollisionEvent(actor2))

    def __geometry_from_actor(self, actor):
        return [self.__normalize_with_position(point, actor.position).as_tuple() for point in actor.hitbox.point_list]

    def __normalize_with_position(self, point, position):
        return point+position
