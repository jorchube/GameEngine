class Audio(object):
    class __SoundEffect(object):
        def __init__(self, backend_data):
            self.backend_data = backend_data

    __audio_delegate = None

    @classmethod
    def initialize(cls, audio_delegate):
        cls.__audio_delegate = audio_delegate

    @classmethod
    def new_sound(cls, file_path):
        backend_data = cls.__audio_delegate.new_sound(file_path)
        return cls.__SoundEffect(backend_data)

    @classmethod
    def play_sound(cls, sound):
        cls.__audio_delegate.play_sound(sound.backend_data)
