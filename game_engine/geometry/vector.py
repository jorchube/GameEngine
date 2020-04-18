import math
from game_engine.geometry.point import Point3D


class Vector3D(Point3D):
    def __init__(self, x, y, z, origin=None):
        if origin is None:
            super().__init__(x, y, z)
        else:
            super().__init__(x-origin.x, y-origin.y, z-origin.z)

    def modulus(self):
        return math.sqrt(self.x**2 + self.y**2)

    @classmethod
    def add_scalar_to_all_components(cls, vector, scalar):
        return Vector3D(vector.x + scalar, vector.y + scalar, vector.z + scalar)

    @classmethod
    def divide_vector_by_number(cls, vector, number):
        x = vector.x / number
        y = vector.y / number
        z = vector.z / number
        return Vector3D(x, y, z)

    @classmethod
    def multiply_vector_by_number(cls, vector, number):
        x = vector.x * number
        y = vector.y * number
        z = vector.z * number
        return Vector3D(x, y, z)