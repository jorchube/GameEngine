class Audio(object):
    class ASound(object):
        __backend_data = None

        def __init__(self, file_path, delegate):
            self.__audio_delegate = delegate
            self.__backend_data = self.__audio_delegate.new_sound(file_path)

        def play(self):
            self.__audio_delegate.play_sound(self.__backend_data)

    __audio_delegate = None

    @classmethod
    def initialize(cls, audio_delegate):
        cls.__audio_delegate = audio_delegate

    @classmethod
    def new_sound(cls, file_path):
        return cls.ASound(file_path, cls.__audio_delegate)
