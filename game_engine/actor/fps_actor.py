from game_engine.actor import Actor
from game_engine.component import TextComponent
from game_engine.game import Game
from game_engine.visual import RGB


class FPSActor(Actor):
    import time

    def __init__(self):
        super().__init__()
        self.__text_component = TextComponent(' ', size=12, fg_color=RGB(0, 0.3, 0))
        self.add_component(self.__text_component)
        self.elapsed_ticks = 0
        self.fps_on_target = True

    def end_tick(self):
        self.elapsed_ticks += 1
        self.__update_fps_string()
        super().end_tick()

    def __update_fps_string(self):
        if '_print_fps_start_ns' not in self.__dict__:
            setattr(self, '_print_fps_start_ns', 0)
        if self.elapsed_ticks % Game.display_configuration().fps == 0:
            fps = int(Game.display_configuration().fps / ((self.time.perf_counter_ns() - self._print_fps_start_ns) / 1000000000))
            fps_string = f'{fps} FPS'
            self._print_fps_start_ns = self.time.perf_counter_ns()
            self.__text_component.text.set_string(fps_string)