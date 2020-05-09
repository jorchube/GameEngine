from game_engine.geometry import Polygon, Point3D, GeometryOperations


class PrimitiveShapes(object):
    @staticmethod
    def triangle(side, rotation=None):
        height = (side / 2) * 0.86
        return PrimitiveShapes._transform_and_return(
            Polygon([
                Point3D(0, height * 0.5, 0),
                Point3D(-side * 0.5, -height * 0.5, 0),
                Point3D(side * 0.5, -height * 0.5, 0),
            ]),
            rotation
        )

    @staticmethod
    def rectangle(width, height, rotation=None):
        return PrimitiveShapes._transform_and_return(
            Polygon([
                Point3D(-width * 0.5, -height * 0.5, 0),
                Point3D(width * 0.5, -height * 0.5, 0),
                Point3D(width * 0.5, height * 0.5, 0),
                Point3D(-width * 0.5, height * 0.5, 0),
            ]),
            rotation
        )

    @staticmethod
    def octogon(radius, rotation=None):
        return PrimitiveShapes._transform_and_return(
            Polygon([
                Point3D(radius, 0, 0),
                Point3D(radius * 0.7, radius * 0.7, 0),
                Point3D(0, radius, 0),
                Point3D(-radius * 0.7, radius * 0.7, 0),
                Point3D(-radius, 0, 0),
                Point3D(-radius * 0.7, -radius * 0.7, 0),
                Point3D(0, -radius, 0),
                Point3D(radius * 0.7, -radius * 0.7, 0),
            ]),
            rotation
        )

    @staticmethod
    def star4arms(outer_radius, inner_radius, rotation=None):
        return PrimitiveShapes._transform_and_return(
            Polygon([
                Point3D(inner_radius, 0, 0),
                Point3D(outer_radius, outer_radius, 0),
                Point3D(0, inner_radius, 0),
                Point3D(-outer_radius, outer_radius, 0),
                Point3D(-inner_radius, 0, 0),
                Point3D(-outer_radius, -outer_radius, 0),
                Point3D(0, -inner_radius, 0),
                Point3D(outer_radius, -outer_radius, 0),
            ]),
            rotation
        )

    @staticmethod
    def _transform_and_return(polygon, rotation):
        if rotation:
            return GeometryOperations.rotate_polygon(polygon, Point3D(0, 0, 0), rotation)
        else:
            return polygon
