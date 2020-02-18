class DisplayConfiguration(object):
    def __init__(self, width_px, height_px):
        self.__width = width_px
        self.__height = height_px

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
