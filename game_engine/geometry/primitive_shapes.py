from game_engine.geometry import Polygon, Point3D


class PrimitiveShapes(object):
    @staticmethod
    def rectangle(width, height):
        return Polygon([
            Point3D(-width * 0.5, -height * 0.5, 0),
            Point3D(width * 0.5, -height * 0.5, 0),
            Point3D(width * 0.5, height * 0.5, 0),
            Point3D(-width * 0.5, height * 0.5, 0),
        ])

    @staticmethod
    def hexagon(radius):
        return Polygon([
            Point3D(0, radius, 0),
            Point3D(-radius * 0.86, radius * 0.5, 0),
            Point3D(-radius * 0.86, -radius * 0.5, 0),
            Point3D(0, -radius, 0),
            Point3D(-radius * 0.86, radius * 0.5, 0),
            Point3D(radius * 0.86, radius * 0.5, 0),
        ])

    @staticmethod
    def octogon(radius):
        return Polygon([
            Point3D(radius, 0, 0),
            Point3D(radius * 0.7, radius * 0.7, 0),
            Point3D(0, radius * 0.7, 0),
            Point3D(-radius * 0.7, radius * 0.7, 0),
            Point3D(-radius, 0, 0),
            Point3D(-radius * 0.7, -radius * 0.7, 0),
            Point3D(0, -radius * 0.7, 0),
            Point3D(radius * 0.7, -radius * 0.7, 0),
        ])

    @staticmethod
    def star4arms(inner_radius, outer_radius):
        return Polygon([
            Point3D(outer_radius, 0, 0),
            Point3D(inner_radius * 0.7, inner_radius * 0.7, 0),
            Point3D(0, outer_radius, 0),
            Point3D(-inner_radius * 0.7, inner_radius * 0.7, 0),
            Point3D(-outer_radius, 0, 0),
            Point3D(-inner_radius * 0.7, -inner_radius * 0.7, 0),
            Point3D(0, -outer_radius, 0),
            Point3D(inner_radius * 0.7, -inner_radius * 0.7, 0),
        ])
