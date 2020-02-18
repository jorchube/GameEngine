from src import game_engine
from src.game_engine import scene
from src.game_engine.actor.player_actor import PlayerActor
from src.game_engine.display_configuration import DisplayConfiguration
from src.game_engine.geometry.point import Point3D


def start_engine_poc():
    fps = 30
    display_width = 800
    display_height = 600

    display_config = DisplayConfiguration(width_px=display_width, height_px=display_height)
    initial_scene = scene.Scene()
    initial_scene.add_actor(PlayerActor([Point3D(0,0,0), Point3D(0,1,0), Point3D(1,0.5,0)]))
    engine = game_engine.default_engine(fps, display_config, initial_scene)

    engine.run_loop()


def main():
    start_engine_poc()


if __name__ == "__main__":
    main()
