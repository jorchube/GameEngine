class AudioDelegateInterface(object):
    def new_sound(self, sound_file):
        raise NotImplementedError

    def play_sound(self, sound):
        raise NotImplementedError


class NewSoundError(RuntimeError):
    pass