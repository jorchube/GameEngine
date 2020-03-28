from src.game_engine.geometry.point import Point3D


class Vector3D(Point3D):
    def __init__(self, x, y, z, origin=None):
        if origin is None:
            super().__init__(x, y, z)
        else:
            super().__init__(x-origin.x, y-origin.y, z-origin.z)

    @classmethod
    def divide_vector_by_number(cls, vector, number):
        x = vector.x / number
        y = vector.y / number
        z = vector.z / number
        return Vector3D(x, y, z)
