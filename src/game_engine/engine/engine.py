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

    def _run_loop(self):
        actors = self._scene.actors()
        self._collision_engine.calculate_collisions(actors)
        self.engine_delegate.digest_events()
        self._process_events()
        self.engine_delegate.clear_display()
        self._draw_actors()
        self._notify_end_tick_to_actors()
        self.engine_delegate.end_tick()

    def _notify_end_tick_to_actors(self):
        for actor in self._scene.actors():
            actor.end_tick()

    def _draw_actors(self):
        for actor in self._scene.actors():
            actor.draw()

    def _process_events(self):
        for event in self._digested_events:
            self._forward_event_to_actors(event)

    def _forward_event_to_actors(self, event):
        for actor in self._scene.actors():
            actor.receive_event(event)

