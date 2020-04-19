from game_engine.actor import Actor
from game_engine.event.event_type import mouse_motion_event


class MouseActor(Actor):
    def __init__(self):
        super().__init__()
        self.subscribe_to_event(mouse_motion_event.MouseMotionEvent, self.__on_mouse_motion_event)

    def __on_mouse_motion_event(self, event):
        from game_engine.game import Game
        self.position.x = event.delta_x  # - Game.display_configuration().width
        self.position.y = event.delta_y  # + Game.display_configuration().height

    def end_tick(self):
        super().end_tick()
