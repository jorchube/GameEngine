from src.game_engine.component.component import Component
from src.game_engine.geometry.operations import GeometryOperations
from src.game_engine import backend


class PolygonComponent(Component):
    def __init__(self, polygon):
        super().__init__()
        self.__draw_delegate = backend.polygon_component_draw_delegate()
        self.__polygon = polygon
        self.__original_polygon = polygon

    def end_tick(self):
        self.__draw_delegate.draw(self.__polygon, self.actor.position)

    def update_rotation(self):
        self.__polygon = GeometryOperations.rotate_polygon(self.__original_polygon, self.actor.position, self.actor.rotation.z_axis)