import time

from src.game_engine import collision_engine
from src.game_engine.game import Game


class Engine(object):
    def __init__(self, display_configuration, initial_scene, engine_delegate):
        self.running = False
        self._scene = initial_scene
        self._display_configuration = display_configuration
        self._collision_engine = collision_engine.CollisionEngine()
        self.engine_delegate = engine_delegate
        self.engine_delegate.initialize(self)
        self._digested_events = []
        Game.set_display_configuration(display_configuration)
        self.elapsed_ticks = 0

    @property
    def display_configuration(self):
        return self._display_configuration

    def set_digested_events(self, events):
        self._digested_events = events

    def set_scene(self, scene):
        self._scene = scene

    def run_loop(self):
        self.running = True
        while self.running:
            self._run_loop()
            self.elapsed_ticks += 1
            self.__print_timing_information()

    def _run_loop(self):
        #actors = self._scene.actors()
        self._collision_engine.calculate_collisions(self._scene.colliding_actors())
        self.engine_delegate.digest_events()
        self._process_events()
        self.engine_delegate.clear_display()
        self._notify_end_tick_to_actors()
        self.engine_delegate.end_tick()

    def _notify_end_tick_to_actors(self):
        for actor in self._scene.actors():
            actor.end_tick()

    def _process_events(self):
        for event in self._digested_events:
            self._forward_event_to_actors(event)

    def _forward_event_to_actors(self, event):
        for actor in self._scene.actors():
            actor.receive_event(event)

    def __print_timing_information(self):
        if '_print_fps_start_ns' not in self.__dict__:
            setattr(self, '_print_fps_start_ns', 0)
        if self.elapsed_ticks % self.display_configuration.fps == 0:
            print(f'>> {self.display_configuration.fps/((time.perf_counter_ns() - self._print_fps_start_ns)/1000000000.0)} FPS')
            print(f'>> tick time: {(1000.0 / self.display_configuration.fps)} ms')
            self._print_fps_start_ns = time.perf_counter_ns()

    def _run_loop_measured(self):
        actors = measure_ns(self._scene.actors)
        measure_ns(self._collision_engine.calculate_collisions, actors)
        measure_ns(self.engine_delegate.digest_events)
        measure_ns(self._process_events)
        measure_ns(self.engine_delegate.clear_display)
        measure_ns(self._draw_actors)
        measure_ns(self._notify_end_tick_to_actors)
        measure_ns(self.engine_delegate.end_tick)
        print('######################################################')

def measure_ns(method, *args, **kwargs):
    def wrapped_func():
        tA = time.perf_counter_ns()
        ret = method(*args, **kwargs)
        tB = time.perf_counter_ns()
        print(f'{method}: {(tB-tA)/1000000.0} ms')
        return ret
    return wrapped_func()
