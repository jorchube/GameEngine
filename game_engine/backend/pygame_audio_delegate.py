from game_engine.audio.audio_delegate import AudioDelegateInterface
from pygame import mixer


class PygameAudioDelegate(AudioDelegateInterface):
    def __init__(self):
        if mixer.get_init() is None:
            mixer.init()
            mixer.set_num_channels(32)

    def new_sound(self, sound_file):
        try:
            return mixer.Sound(sound_file)
        except Exception as exc:
            print('Unable to create new sound: {msg}'.format(msg=exc))

    def play_sound(self, sound):
        sound.play()

