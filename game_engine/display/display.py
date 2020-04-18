from game_engine.display.display_configuration import DisplayConfiguration


class Display(object):
    __configuration = None

    @classmethod
    def set_configuration(cls, configuration):
        if type(configuration) != DisplayConfiguration:
            raise DisplayError('Unable to set display configuration with an object of type {t}'.format(t=type(configuration)))
        cls.__configuration = configuration

    @classmethod
    def configure(cls, width_px, height_px, fps, scaled=False):
        cls.set_configuration(DisplayConfiguration(width_px, height_px, fps, scaled))

    @classmethod
    def configuration(cls):
        return cls.__configuration


class DisplayError(RuntimeError):
    pass