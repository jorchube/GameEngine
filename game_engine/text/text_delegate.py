class TextDelegateInterface(object):
    def new_text(self, string, font_size):
        raise NotImplementedError

    def draw_text(self, text, position):
        raise NotImplementedError
