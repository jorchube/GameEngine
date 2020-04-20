import random

from game_engine import scene
from game_engine.actor.actor import Actor
from game_engine.actor.mouse_actor import MouseActor
from game_engine.actor.particle import Particle
from game_engine.actor.player_actor import PlayerActor
from game_engine.audio.audio import Audio
from game_engine.component.move_component import MoveComponentNode, MoveComponent
from game_engine.component.shoot_pattern_component import ShootPatternComponent, ShootPatternComponentNode
from game_engine.geometry import Rotation
from game_engine.component.color_component import ColorComponent
from game_engine.component.hitbox_component import HitboxComponent
from game_engine.component.outline_component import OutlineComponent
from game_engine.component.particle_emitter_component import ParticleEmitterComponent
from game_engine.component.polygon_component import PolygonComponent
from game_engine.component.text_component import TextComponent
from game_engine.display.display_configuration import DisplayConfiguration
from game_engine.event.event_type import collision_event
from game_engine.game import Game
from game_engine.geometry.point import Point3D
from game_engine.geometry.polygon import Polygon
from game_engine.geometry.vector import Vector3D
from game_engine.visual.camera import Camera
from game_engine.visual.rgb import RGB


def start_engine_poc():
    display_config = DisplayConfiguration(width_px=800, height_px=600, fps=60, scaled=True)
    camera = Camera(Point3D(0, 0, -50), Rotation(0, 0, 0), 45, 0.1, 100.0)
    initial_scene = scene.Scene()
    Game.initialize(display_config, camera, initial_scene)
    __add_some_actors(initial_scene)
    Game.run()


def __add_some_actors(_scene):
    _scene.add_actor(APlayerActor())
    _scene.add_actor(RotatingTriangle())
    _scene.add_actor(RotatingSquare())
    _scene.add_actor(ColoredSquare())
    _scene.add_actor(ColoredAndOutlinedSquare())
    _scene.add_actor(EmitterActor())
    _scene.add_actor(VeryCompoundActor())
    _scene.add_actor(FPSActor())
    _scene.add_actor(MovingActor())
    # _scene.add_actor(AMouseActor())  # This one is not nearly finished


class APlayerActor(PlayerActor):
    def __init__(self):
        super().__init__()
        self.rgb = RGB(1, 1, 1)
        polygon = Polygon([Point3D(0, 0, 0), Point3D(0, 1, 0), Point3D(1, 0.5, 0)])
        self.add_component(PolygonComponent(polygon))
        self.add_component(HitboxComponent(polygon, is_collision_source=True))
        self.add_component(ColorComponent(self.rgb))
        self.subscribe_to_event(collision_event.CollisionEvent, self.__on_collision_event)
        self.collision_sound = Audio.new_sound('sound_samples/rubber_ducky.wav')
        self.__collision_timeout = 0
        self.collision_mask = 0x01

    def __on_collision_event(self, event):
        self.rgb.blue = 0
        self.rgb.green = 0
        if self.__collision_timeout <= 0:
            self.collision_sound.play()
        self.__collision_timeout = 0.1

    def end_tick(self):
        super().end_tick()
        if self.__collision_timeout > 0:
            self.__decrease_collision_timeout()

    def __decrease_collision_timeout(self):
        self.__collision_timeout -= (1/Game.display_configuration().fps)
        if self.__collision_timeout <= 0:
            self.rgb.blue = 1
            self.rgb.green = 1


class AMouseActor(MouseActor):
    def __init__(self):
        super().__init__()
        self.rgb = RGB(0, 1, 0)
        polygon = Polygon([Point3D(0, 0, 0), Point3D(0, 1, 0), Point3D(1, 0.5, 0)])
        self.add_component(PolygonComponent(polygon))
        self.add_component(HitboxComponent(polygon, is_collision_source=True))
        self.add_component(ColorComponent(self.rgb))
        self.position.x = 15
        self.position.y = 15


class RotatingTriangle(Actor):
    def __init__(self):
        super().__init__()
        body = Polygon([Point3D(5, 0, 0), Point3D(0, 5, 0), Point3D(5, 5, 0)])

        body.translate(Vector3D(0, 0, 0, origin=body.center))

        self.add_component(HitboxComponent(body))
        self.add_component(PolygonComponent(body))
        self.position = Point3D(-15, 5, 0)
        self.spinning_speed = 3


class RotatingSquare(Actor):
    def __init__(self):
        super().__init__()
        body = Polygon([Point3D(-2.5, -2.5, 0), Point3D(2.5, -2.5, 0), Point3D(2.5, 2.5, 0), Point3D(-2.5, 2.5, 0)])
        self.add_component(HitboxComponent(body))
        self.add_component(PolygonComponent(body))
        self.position = Point3D(15, -10, 0)
        self.spinning_speed = -5


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


class EmitterActor(Actor):
    def __init__(self):
        super().__init__()
        body = Polygon([Point3D(0, 0, 0), Point3D(-3, -1, 0), Point3D(-3, 1, 0)])
        self.add_component(HitboxComponent(body))
        self.add_component(PolygonComponent(body))
        self.position = Point3D(-10, 15, 0)
        particle_emitter = ParticleEmitterComponent(
            TriangleParticle,
            10,
            Vector3D(6, 0, 0),
            speed_variability=0.5,
            direction_variability=60
        )
        self.add_component(particle_emitter)


class TriangleParticle(Particle):
    def __init__(self):
        lifespan = random.uniform(0.5, 2)
        super().__init__(lifespan)
        self.add_component(PolygonComponent(Polygon([Point3D(-0.05, 0, 0), Point3D(0.05, 0.1, 0), Point3D(0.05, -0.1, 0)])))
        self.add_component(ColorComponent(RGB(0.3, 0.7, 0.3)))


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
        self.spinning_speed = 0.6
        self.subscribe_to_event(collision_event.CollisionEvent, self.__on_collision_event)
        self.collision_sound = Audio.new_sound('sound_samples/metal_crunch.wav')
        particle_emitter = ParticleEmitterComponent(
            RotatingParticle,
            5,
            Vector3D(9, 0, 0),
            speed_variability=0.1,
            direction_variability=0.1
        )
        particle_emitter.position_offset_relative_to_actor = Vector3D(5, 0, 0)
        self.add_component(particle_emitter)
        self.collision_mask = 0x01

    def __on_collision_event(self, event):
        self.collision_sound.play()


class RotatingParticle(Particle):
    def __init__(self):
        lifespan = random.uniform(2, 4)
        super().__init__(lifespan)
        body = Polygon([Point3D(-0.1, 0, 0), Point3D(0.1, 0.2, 0), Point3D(0.1, -0.2, 0)])
        self.add_component(PolygonComponent(body))
        self.add_component(HitboxComponent(body))
        self.add_component(ColorComponent(RGB(0.3, 0.7, 0.3)))
        self.spinning_speed = 30
        self.collision_mask = 0x01


class FPSActor(Actor):
    import time

    def __init__(self):
        super().__init__()
        self.__text_component = TextComponent(' ', size=12, fg_color=RGB(0, 0.3, 0))
        self.add_component(self.__text_component)
        self.position = Point3D(25, -20, 0)
        self.elapsed_ticks = 0
        self.fps_on_target = True

    def end_tick(self):
        self.elapsed_ticks += 1
        self.__update_fps_string()
        super().end_tick()

    def __update_fps_string(self):
        if '_print_fps_start_ns' not in self.__dict__:
            setattr(self, '_print_fps_start_ns', 0)
        if self.elapsed_ticks % Game.display_configuration().fps == 0:
            fps = int(Game.display_configuration().fps / ((self.time.perf_counter_ns() - self._print_fps_start_ns) / 1000000000))
            fps_string = f'{fps} FPS'
            self._print_fps_start_ns = self.time.perf_counter_ns()
            if fps < 58:
                if self.fps_on_target:
                    self.fps_on_target = False
                    self.__text_component.text.set_fg_color(RGB(0.3, 0, 0))
            if fps >= 58:
                if not self.fps_on_target:
                    self.fps_on_target = True
                    self.__text_component.text.set_fg_color(RGB(0, 0.3, 0))
            self.__text_component.text.set_string(fps_string)


class MovingActor(Actor):
    def __init__(self):
        super().__init__()
        body = Polygon([Point3D(0, 0, 0), Point3D(3, 1, 0), Point3D(3, -1, 0)])
        self.add_component(PolygonComponent(body))
        self.position = Point3D(10, 10, 0)
        self.add_component(ColorComponent(RGB(0.2, 0.2, 1)))
        movement_node_list = [
            MoveComponentNode(Vector3D(-5, 0, 0), 1),
            MoveComponentNode(Vector3D(0, -5, 0), 1),
            MoveComponentNode(Vector3D(5, 0, 0), 1),
            MoveComponentNode(Vector3D(0, 5, 0), 1),
        ] * 50
        self.add_component(MoveComponent(movement_node_list))
        particle_emitter = ParticleEmitterComponent(
            RotatingParticle,
            10,
            Vector3D(-6, 0, 0),
            speed_variability=0,
            direction_variability=0
        )
        shoot_pattern_node_list = [ShootPatternComponentNode(particle_emitter, 0.3),
                                   ShootPatternComponentNode(None, 0.3)] * 999
        self.add_component(ShootPatternComponent(shoot_pattern_node_list))


def main():
    start_engine_poc()


if __name__ == "__main__":
    main()
