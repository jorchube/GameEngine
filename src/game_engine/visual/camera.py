class Camera(object):
    def __init__(self, position, rotation, fov, near_clipping_distance=1, far_clipping_distance=100):
        self.position = position
        self.rotation = rotation
        self.fov = fov
        self.near_clipping_distance = near_clipping_distance
        self.far_clipping_distance = far_clipping_distance
