from src.game_engine import backend
from src.game_engine.actor.player_actor import PlayerActor
from src.game_engine.actor.polygon_actor import PolygonActor


class ActorFactory(object):
    @classmethod
    def new_polygon_actor(cls, point_list):
        return PolygonActor(point_list, backend.polygon_actor_draw_delegate())

    @classmethod
    def new_player_actor(cls, point_list):
        actor = PlayerActor(point_list, backend.polygon_actor_draw_delegate())
        actor.check_collisions = True
        return actor

