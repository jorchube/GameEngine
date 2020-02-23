class Game(object):
    __display_configuration = None

    @classmethod
    def display_configuration(cls):
        return cls.__display_configuration

    @classmethod
    def set_display_configuration(cls, display_configuration):
        cls.__display_configuration = display_configuration

