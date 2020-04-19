from game_engine import backend
from game_engine import audio
from game_engine import engine
from game_engine import text
from game_engine.display.display import Display
from game_engine.event import event_handler
from game_engine.event.event_type.particle_expired_event import ParticleExpiredEvent
from game_engine.event.event_type.quit_event import QuitEvent


class Game(object):
    __camera = None
    __scene = None
    __engine = None

    __event_handler = None

    @classmethod
    def initialize(cls, display_configuration, camera, initial_scene):
        cls.__initialize_event_handler()
        Display.set_configuration(display_configuration)
        cls.__camera = camera
        cls.__scene = initial_scene
        audio.Audio.initialize(backend.audio_delegate())
        text.Text.initialize(backend.text_delegate())
        cls.__engine = engine.Engine(camera, display_configuration, initial_scene, backend.engine_delegate())

    @classmethod
    def __initialize_event_handler(cls):
        cls.__event_handler = event_handler.EventHandler()
        cls.__subscribe_to_event(QuitEvent, cls.__quit_event_received)
        cls.__subscribe_to_event(ParticleExpiredEvent, cls.__particle_expired_event)

    @classmethod
    def run(cls):
        cls.__engine.run_loop()

    @classmethod
    def display_configuration(cls):
        return Display.configuration()

    @classmethod
    def set_display_configuration(cls, display_configuration):
        Display.set_configuration(display_configuration)

    @classmethod
    def set_scene(cls, scene):
        cls.__scene = scene

    @classmethod
    def __subscribe_to_event(cls, event_type, callback):
        cls.__event_handler.subscribe(event_type, callback)

    @classmethod
    def receive_event(cls, event):
        cls.__event_handler.event(event)

    @classmethod
    def current_scene(cls):
        return cls.__scene

    @classmethod
    def __particle_expired_event(cls, event):
        cls.current_scene().remove_actor(event.particle)

    @classmethod
    def __quit_event_received(cls, event):
        exit(0)
