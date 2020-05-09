from game_engine.actor.actor import Actor
from game_engine.event.event_type import key_event
from game_engine.event.event_type import collision_event


class _PlayerActorMovementState(object):
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False


class PlayerActor(Actor):
    __move_keys = {
        'up': None,
        'down': None,
        'left': None,
        'right': None,
    }

    def __init__(self):
        super().__init__()
        self.__move_with_wasd = False
        self.__move_speed = 15
        self.__initialize_movement_keys()
        self.movement_state = _PlayerActorMovementState()
        self.subscribe_to_event(key_event.KeyEventPress, self.__on_key_press_event)
        self.subscribe_to_event(key_event.KeyEventRelease, self.__on_key_release_event)
        self.subscribe_to_event(collision_event.CollisionEvent, self.__on_collision_event)

    @property
    def move_with_wasd(self):
        return self.__move_with_wasd

    @move_with_wasd.setter
    def move_with_wasd(self, value):
        self.__move_with_wasd = value

    @property
    def move_speed(self):
        return self.__move_speed

    @move_speed.setter
    def move_speed(self, value):
        self.__move_speed = value

    def end_tick(self):
        self.__update_move_vector()
        super().end_tick()

    def __initialize_movement_keys(self):
        if self.move_with_wasd:
            self.__move_keys['up'] = key_event.Key.W
            self.__move_keys['down'] = key_event.Key.S
            self.__move_keys['left'] = key_event.Key.A
            self.__move_keys['right'] = key_event.Key.D
        else:
            self.__move_keys['up'] = key_event.Key.UP_ARROW
            self.__move_keys['down'] = key_event.Key.DOWN_ARROW
            self.__move_keys['left'] = key_event.Key.LEFT_ARROW
            self.__move_keys['right'] = key_event.Key.RIGHT_ARROW

    def __on_collision_event(self, event):
        pass

    def __on_key_press_event(self, event):
        if event.key in self.__move_keys.values():
            self.__update_movement_state(event.key, True)

    def __on_key_release_event(self, event):
        if event.key in self.__move_keys.values():
            self.__update_movement_state(event.key, False)

    def __update_movement_state(self, key, value):
        if key == self.__move_keys['up']:
            self.movement_state.up = value
        if key == self.__move_keys['down']:
            self.movement_state.down = value
        if key == self.__move_keys['left']:
            self.movement_state.left = value
        if key == self.__move_keys['right']:
            self.movement_state.right = value

    def __update_move_vector(self):
        self.move_vector.y = (self.__move_speed if self.movement_state.up else 0) - (self.__move_speed if self.movement_state.down else 0)
        self.move_vector.x = (self.__move_speed if self.movement_state.right else 0) - (self.__move_speed if self.movement_state.left else 0)
