from game_engine.actor.player_actor import PlayerActor
from game_engine.actor.actor import Actor
from game_engine.component.hitbox_component import HitboxComponent
from game_engine.component.polygon_component import PolygonComponent


class ActorFactory(object):
    @classmethod
    def new_player_actor(cls, polygon):
        actor = PlayerActor()
        actor.add_component(PolygonComponent(polygon))
        actor.add_component(HitboxComponent(polygon, is_collision_source=True))
        return actor

    @classmethod
    def new_polygon_actor(cls, polygon):
        actor = Actor()
        actor.add_component(PolygonComponent(polygon))
        actor.add_component(HitboxComponent(polygon, is_collision_source=False))
        return actor
