from src.game_engine import backend
from src.game_engine import scene
from src.game_engine.engine.engine import Engine
from src.game_engine.actor.actor_factory import ActorFactory
from src.game_engine.display_configuration import DisplayConfiguration
from src.game_engine.geometry.point import Point3D
from src.game_engine.geometry.polygon import Polygon


def start_engine_poc():
    display_config = DisplayConfiguration(width_px=800, height_px=600, fps=60)
    initial_scene = scene.Scene()
    initial_scene.add_actor(ActorFactory.new_player_actor(Polygon([Point3D(0, 0, 0), Point3D(0, 1, 0), Point3D(1, 0.5, 0)])))
    initial_scene.add_actor(ActorFactory.new_polygon_actor(Polygon([Point3D(5, 0, 0), Point3D(0, 5, 0), Point3D(5, 5, 0)])))
    # for i in range(-30, 30):
    #     actor = ActorFactory.new_polygon_actor(Polygon([Point3D(0.2, 0, 0), Point3D(0.2, 0.2, 0), Point3D(0, 0.2, 0), Point3D(0, 0, 0)]))
    #     actor.position = Point3D(i, i, 0)
    #     initial_scene.add_actor(actor)

    engine = Engine(display_config, initial_scene, backend.engine_delegate())

    engine.run_loop()


def main():
    start_engine_poc()


if __name__ == "__main__":
    main()
