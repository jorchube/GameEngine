import threading
import time

from game_engine import collision_engine
from game_engine.event.event_dispatcher import EventDispatcher


class Engine(object):
    def __init__(self, camera, display_configuration, initial_scene, engine_delegate):
        self._display_configuration = display_configuration
        self.running = False
        self._scene = initial_scene
        self.__update_scene_loop_thread = threading.Thread(target=self.__update_scene_loop_thread)
        self.__update_scene_loop_lock = threading.Lock()
        self.__run_loop_lock = threading.Lock()
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
        return self._scene

    def run_loop(self):
        self.running = True
        self.__update_scene_loop_lock.acquire()
        self.__run_loop_lock.acquire()
        self.__update_scene_loop_thread.start()
        while self.running:
            self._run_loop()

    def _run_loop(self):
        self.__update_scene_loop_lock.release()
        self._clear_display()
        self.__run_loop_lock.acquire()
        self._draw_scene()
        self._end_tick()

    def _draw_scene(self):
        self._scene.draw()

    def _end_tick(self):
        self.engine_delegate.end_tick()
        self.__elapsed_ticks += 1

    def _clear_display(self):
        self.engine_delegate.clear_display()

    def _update_scene_loop(self):
        self.__calculate_collisions()
        self.engine_delegate.digest_events()
        self._process_events()
        self._scene.end_tick()

    def __update_scene_loop_thread(self):
        while self.running:
            self.__update_scene_loop_lock.acquire()
            self._update_scene_loop()
            self.__run_loop_lock.release()

    def __calculate_collisions(self):
        self._collision_engine.calculate_collisions(self._scene.colliding_actors())

    def _process_events(self):
        EventDispatcher.append_event_list(self._digested_events)
        EventDispatcher.dispatch_events()

    def shutdown(self):
        self.running = False
        if self.__update_scene_loop_lock.locked():
            self.__update_scene_loop_lock.release()
        if self.__run_loop_lock.locked():
            self.__run_loop_lock.release()