from src.game_engine import backend
from src.game_engine import scene
from src.game_engine.actor.actor import Actor
from src.game_engine.component.color_component import ColorComponent
from src.game_engine.component.hitbox_component import HitboxComponent
from src.game_engine.component.outline_component import OutlineComponent
from src.game_engine.component.polygon_component import PolygonComponent
from src.game_engine.engine.engine import Engine
from src.game_engine.actor.actor_factory import ActorFactory
from src.game_engine.display_configuration import DisplayConfiguration
from src.game_engine.geometry.point import Point3D
from src.game_engine.geometry.polygon import Polygon
from src.game_engine.geometry.vector import Vector3D
from src.game_engine.visual.rgb import RGB


def start_engine_poc():
    display_config = DisplayConfiguration(width_px=800, height_px=600, fps=60)
    initial_scene = scene.Scene()
    __add_some_actors(initial_scene)
    engine = Engine(display_config, initial_scene, backend.engine_delegate())
    engine.run_loop()


def __add_some_actors(_scene):
    player_actor = ActorFactory.new_player_actor(Polygon([Point3D(0, 0, 0), Point3D(0, 1, 0), Point3D(1, 0.5, 0)]))
    _scene.add_actor(player_actor)

    another_actor = ActorFactory.new_polygon_actor(Polygon([Point3D(5, 0, 0), Point3D(0, 5, 0), Point3D(5, 5, 0)]))
    _scene.add_actor(another_actor)

    for i in range(-30, 30):
        actor = ActorFactory.new_polygon_actor(Polygon([Point3D(1, -0.1, 0), Point3D(1, 0.1, 0), Point3D(-1, 0.1, 0), Point3D(-1, -0.1, 0)]))
        actor.rotation.z_axis += i*12
        actor.position = Point3D(i, i, 0)
        _scene.add_actor(actor)

    _scene.add_actor(RotatingTriangle())
    _scene.add_actor(RotatingSquare())
    _scene.add_actor(ColoredSquare())
    _scene.add_actor(ColoredAndOutlinedSquare())
    _scene.add_actor(VeryCompoundActor())


class RotatingTriangle(Actor):
    def __init__(self):
        super().__init__()
        body = Polygon([Point3D(5, 0, 0), Point3D(0, 5, 0), Point3D(5, 5, 0)])

        body.translate(Vector3D(0, 0, 0, origin=body.center))

        self.add_component(HitboxComponent(body))
        self.add_component(PolygonComponent(body))
        self.position = Point3D(-15, 5, 0)

    def end_tick(self):
        self.rotation.z_axis += 1
        super().end_tick()


class RotatingSquare(Actor):
    def __init__(self):
        super().__init__()
        body = Polygon([Point3D(-2.5, -2.5, 0), Point3D(2.5, -2.5, 0), Point3D(2.5, 2.5, 0), Point3D(-2.5, 2.5, 0)])
        self.add_component(HitboxComponent(body))
        self.add_component(PolygonComponent(body))
        self.position = Point3D(15, -10, 0)

    def end_tick(self):
        self.rotation.z_axis -= 5
        super().end_tick()


class ColoredSquare(Actor):
    def __init__(self):
        super().__init__()
        body = Polygon([Point3D(-1, -1, 0), Point3D(1, -1, 0), Point3D(1, 1, 0), Point3D(-1, 1, 0)])
        self.add_component(ColorComponent(RGB(1, 0, 0.5)))
        self.add_component(HitboxComponent(body))
        self.add_component(PolygonComponent(body))
        self.position = Point3D(0, 10, 0)


class ColoredAndOutlinedSquare(Actor):
    def __init__(self):
        super().__init__()
        body = Polygon([Point3D(-1, -1, 0), Point3D(1, -1, 0), Point3D(1, 1, 0), Point3D(-1, 1, 0)])
        self.add_component(ColorComponent(RGB(0, 0.7, 0)))
        self.add_component(OutlineComponent(RGB(1, 0, 0), thickness=4))
        self.add_component(HitboxComponent(body))
        self.add_component(PolygonComponent(body))
        self.position = Point3D(-3, 8, 0)


class VeryCompoundActor(Actor):
    def __init__(self):
        super().__init__()
        body1 = Polygon([Point3D(0, -0.25, 0), Point3D(3, -0.25, 0), Point3D(3, 0.25, 0), Point3D(0, 0.25, 0)])
        body2 = Polygon([Point3D(3.5, -1, 0), Point3D(3.5, 1, 0), Point3D(5, 0, 0)])
        polygon1 = PolygonComponent(body1)
        polygon1.add_component(ColorComponent(RGB(1, 0, 0)))
        polygon1.add_component(OutlineComponent(RGB(0, 0, 1), thickness=4))
        polygon2 = PolygonComponent(body2)
        polygon2.add_component(ColorComponent(RGB(0, 1, 0)))
        polygon2.add_component(OutlineComponent(RGB(0.5, 0, 0.5), thickness=8))
        self.add_component(HitboxComponent(body1))
        self.add_component(polygon1)
        self.add_component(HitboxComponent(body2))
        self.add_component(polygon2)
        self.position = Point3D(5, -15, 0)

    def end_tick(self):
        self.rotation.z_axis -= 1
        super().end_tick()



def main():
    start_engine_poc()


if __name__ == "__main__":
    main()
