class EngineDelegate(object):
    def initialize(self, engine):
        raise NotImplementedError

    def digest_events(self, engine):
        raise NotImplementedError

    def clear_display(self):
        raise NotImplementedError

    def end_tick(self):
        raise NotImplementedError
