from src.game_engine import collision_engine


class Engine(object):
    def __init__(self, framerate, display_configuration, initial_scene):
        self.running = False
        self._scene = initial_scene
        self._framerate = framerate
        self._display = display_configuration
        self._collision_engine = collision_engine.CollisionEngine()

    def set_scene(self, scene):
        self._scene = scene

    def run_loop(self):
        self.running = True
        while self.running:
            self._run_loop()

    def _run_loop(self):
        actors = self._scene.actors()
        self._collision_engine.calculate_collisions(actors)
        self._process_events()
        self._end_tick()

    def _process_events(self):
        raise NotImplementedError

    def _end_tick(self):
        raise NotImplementedError
