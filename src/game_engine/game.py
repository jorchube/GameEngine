from src.game_engine import backend
from src.game_engine import audio
from src.game_engine import engine
from src.game_engine import text


class Game(object):
    __display_configuration = None
    __camera = None
    __scene = None
    __engine = None

    @classmethod
    def initialize(cls, display_configuration, camera, initial_scene):
        cls.__display_configuration = display_configuration
        cls.__camera = camera
        cls.__scene = initial_scene
        audio.Audio.initialize(backend.audio_delegate())
        text.Text.initialize(backend.text_delegate())
        cls.__engine = engine.Engine(camera, display_configuration, initial_scene, backend.engine_delegate())

    @classmethod
    def run(cls):
        cls.__engine.run_loop()


    @classmethod
    def display_configuration(cls):
        return cls.__display_configuration

    @classmethod
    def set_display_configuration(cls, display_configuration):
        cls.__display_configuration = display_configuration

