from src.game_engine.actor.polygon_actor import PolygonActor
from src.game_engine.event.event_type import key_event
from src.game_engine.event.event_type import collision_event


class PlayerActor(PolygonActor):
    def __init__(self, point_list, draw_delegate=None):
        super().__init__(point_list, draw_delegate)
        self.subscribe_to_event(key_event.KeyEventPress, self.__on_key_press_event)
        self.subscribe_to_event(collision_event.CollisionEvent, self.__on_collision_event)

    def __on_collision_event(self, event):
        print('Collision with {actor}'.format(actor=event.colliding_actor))

    def __on_key_press_event(self, event):
        if event.key in PlayerActor.__arrow_keys:
            self.__move_with_arrow_key(event.key)

    def __move_with_arrow_key(self, key):
        if key == key_event.Key.UP_ARROW:
            self.position.y = self.position.y + 1
        if key == key_event.Key.DOWN_ARROW:
            self.position.y = self.position.y - 1
        if key == key_event.Key.LEFT_ARROW:
            self.position.x = self.position.x - 1
        if key == key_event.Key.RIGHT_ARROW:
            self.position.x = self.position.x + 1

    __arrow_keys = [
        key_event.Key.UP_ARROW,
        key_event.Key.DOWN_ARROW,
        key_event.Key.LEFT_ARROW,
        key_event.Key.RIGHT_ARROW,
    ]