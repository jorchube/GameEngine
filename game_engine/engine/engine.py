import time

from game_engine import collision_engine
from game_engine.event.event_dispatcher import EventDispatcher


class Engine(object):
    def __init__(self, camera, display_configuration, initial_scene, engine_delegate):
        self._display_configuration = display_configuration
        self.running = False
        self._scene = initial_scene
        self._collision_engine = collision_engine.CollisionEngine()
        self.engine_delegate = engine_delegate
        self.engine_delegate.initialize(self, camera)
        self._digested_events = []
        self.__elapsed_ticks = 0

    @property
    def display_configuration(self):
        return self._display_configuration

    @property
    def elapsed_ticks(self):
        return self.__elapsed_ticks

    def set_digested_events(self, events):
        self._digested_events = events

    def set_scene(self, scene):
        self._scene = scene

    def get_scene(self):
        return self.__scene

    def run_loop(self):
        self.running = True
        while self.running:
            self._run_loop()

    def _run_loop(self):
        self._collision_engine.calculate_collisions(self._scene.colliding_actors())
        self.engine_delegate.digest_events()
        self._process_events()
        self.engine_delegate.clear_display()
        self._notify_end_tick_to_actors()
        self.engine_delegate.end_tick()
        self.__elapsed_ticks += 1

    def _notify_end_tick_to_actors(self):
        for actor in self._scene.actors():
            actor.end_tick()

    def _process_events(self):
        EventDispatcher.append_event_list(self._digested_events)
        EventDispatcher.dispatch_events()

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
