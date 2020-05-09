from game_engine.component.component import Component
from game_engine.component.color_component import ColorComponent
from game_engine.component.outline_component import OutlineComponent
from game_engine.geometry.operations import GeometryOperations
from game_engine import backend


class PolygonComponent(Component):
    def __init__(self, polygon):
        super().__init__()
        self.__draw_delegate = backend.polygon_component_draw_delegate()
        self.__polygon = polygon
        self.__original_polygon = polygon

    def end_tick(self):
        pass

    def draw(self):
        self.__draw_delegate.draw(self.__polygon,
                                  self.actor.position,
                                  rgb_fill=self.__get_rgb_fill_color(),
                                  rgb_outline=self.__get_rgb_outline_color(),
                                  outline_thickness=self.__get_outline_thickness()
                                  )

    def update_rotation(self):
        super().update_rotation()
        self.__polygon = GeometryOperations.rotate_polygon(self.__original_polygon, self.actor.position, self.actor.rotation.z_axis)

    def __get_rgb_fill_color(self):
        return self.__get_rgb_color(ColorComponent)

    def __get_rgb_outline_color(self):
        return self.__get_rgb_color(OutlineComponent)

    def __get_outline_thickness(self):
        if self.__has_component(self, OutlineComponent):
            return (self.components(by_class=OutlineComponent)[0]).thickness
        if self.__has_component(self.actor, OutlineComponent):
            return (self.actor.components(by_class=OutlineComponent)[0]).thickness
        return None

    def __get_rgb_color(self, component_class):
        if self.__has_component(self, component_class):
            return (self.components(by_class=component_class)[0]).rgb
        if self.__has_component(self.actor, component_class):
            return (self.actor.components(by_class=component_class)[0]).rgb
        return None

    def __has_component(self, _object, component_class):
        return len(_object.components(by_class=component_class)) > 0
