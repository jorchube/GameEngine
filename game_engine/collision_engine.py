from game_engine.event.event_type.collision_event import CollisionEvent
from game_engine.geometry.operations import GeometryOperations
from game_engine.component.hitbox_component import HitboxComponent


class CollisionEngine(object):
    def calculate_collisions(self, actors):
        hitbox_components = self.__get_all_hitbox_components(actors)
        collision_sources = list(filter(lambda hb: hb.is_collision_source, hitbox_components))

        while collision_sources:
            collider = collision_sources.pop()
            for hitbox in hitbox_components:
                if self.__check_collision(collider, hitbox):
                    self.__notify_colliding_actors(collider.actor, hitbox.actor)

    def __check_collision(self, hb1, hb2):
        if hb1 is hb2:
            return False
        return self.__hitboxes_collide(hb1, hb2)

    def __hitboxes_collide(self, hb1, hb2):
        return GeometryOperations.are_intersecting_polygons(
            hb1.hitbox, hb1.position,
            hb2.hitbox, hb2.position)

    def __get_all_hitbox_components(self, actors):
        hitbox_components = []
        for actor in actors:
            hitbox_components.extend(actor.components(by_class=HitboxComponent))
        return hitbox_components

    def __notify_colliding_actors(self, actor1, actor2):
        self.__notify_collision(actor1, actor2)
        self.__notify_collision(actor2, actor1)

    def __notify_collision(self, actor1, actor2):
        actor1.receive_event(CollisionEvent(actor2))

