import math
from shapely.geometry import Polygon as sPol
from shapely import affinity
from shapely import geometry
from game_engine.geometry.polygon import Polygon
from game_engine.geometry.point import Point3D
from game_engine.geometry.vector import Vector3D


class GeometryOperations(object):
    @classmethod
    def rotate_polygon(cls, polygon, position, z_axis):
        _geometry = cls.__geometry_from_polygon_and_position(polygon, position)
        return cls.__to_polygon(affinity.rotate(_geometry, z_axis, origin=(position.x, position.y)), position)

    @classmethod
    def rotate_vector(cls, vector, z_axis):
        geo = geometry.LineString([[0, 0, 0], [vector.x, vector.y, vector.z]])
        rotated = affinity.rotate(geo, z_axis)
        new_coords = rotated.coords
        return Vector3D(new_coords[1][0]-new_coords[0][0], new_coords[1][1]-new_coords[0][1], 0)

    @classmethod
    def polygon_center(cls, polygon):
        _geometry = cls.__geometry_from_polygon_and_position(polygon, Point3D(0, 0, 0))
        return Point3D(_geometry.centroid.x, _geometry.centroid.y, 0)

    @classmethod
    def are_intersecting_polygons(cls, polygon1, position1, polygon2, position2):
        _geometry1 = cls.__geometry_from_polygon_and_position(polygon1, position1)
        _geometry2 = cls.__geometry_from_polygon_and_position(polygon2, position2)
        return sPol(_geometry1).intersects(sPol(_geometry2))

    @classmethod
    def __geometry_from_polygon_and_position(cls, polygon, position):
        return geometry.Polygon([cls.__place_polygon_in_position(point, position).as_tuple() for point in polygon.point_list])

    @classmethod
    def __place_polygon_in_position(cls, point, position):
        return point + position

    @classmethod
    def __decouple_point_from_position(cls, point, position):
        return point - position

    @classmethod
    def __to_polygon(cls, _geometry, position):
        _polygon = Polygon([
            cls.__decouple_point_from_position(Point3D(point_2d_tuple[0], point_2d_tuple[1], 0), position)
            for point_2d_tuple in _geometry.exterior.coords
        ])
        return _polygon
