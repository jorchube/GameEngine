from src.game_engine import backend
from src.game_engine import scene
from src.game_engine.actor.actor import Actor
from src.game_engine.component.hitbox_component import HitboxComponent
from src.game_engine.component.polygon_component import PolygonComponent
from src.game_engine.engine.engine import Engine
from src.game_engine.actor.actor_factory import ActorFactory
from src.game_engine.display_configuration import DisplayConfiguration
from src.game_engine.geometry.point import Point3D
from src.game_engine.geometry.polygon import Polygon
from src.game_engine.geometry.vector import Vector3D


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
    _scene.add_actor(RotatingCompoundActor())


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


class RotatingCompoundActor(Actor):
    def __init__(self):
        super().__init__()
        body1 = Polygon([Point3D(0, -0.25, 0), Point3D(3, -0.25, 0), Point3D(3, 0.25, 0), Point3D(0, 0.25, 0)])
        body2 = Polygon([Point3D(3.5, -1, 0), Point3D(3.5, 1, 0), Point3D(5, 0, 0)])
        self.add_component(HitboxComponent(body1))
        self.add_component(PolygonComponent(body1))
        self.add_component(HitboxComponent(body2))
        self.add_component(PolygonComponent(body2))
        self.position = Point3D(5, -15, 0)

    def end_tick(self):
        self.rotation.z_axis -= 1
        super().end_tick()


def main():
    start_engine_poc()


if __name__ == "__main__":
    main()
