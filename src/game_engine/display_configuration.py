class DisplayConfiguration(object):
    def __init__(self, width_px, height_px, fps):
        self.__width = width_px
        self.__height = height_px
        self.__fps = fps

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def fps(self):
        return self.__fps
