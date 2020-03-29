from OpenGL.GL import *
from OpenGL.GLU import *


def check_requirements():
    return bool(gluPerspective)


def clear_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


def push_matrix():
    glPushMatrix()


def pop_matrix():
    glPopMatrix()


def end():
    glEnd()


def begin_polygon():
    glBegin(GL_POLYGON)


def vertex_3fv(point_tuple):
    glVertex3fv(point_tuple)


def gl_translate_f(point):
    glTranslatef(point.x, point.y, point.z)


def gl_rotate_f(x_axis, y_axis, z_axis):
    glRotatef(x_axis, 1, 0, 0)
    glRotatef(y_axis, 0, 1, 0)
    glRotatef(z_axis, 0, 0, 1)


def glu_perspective(fov, aspect_ratio, near_clipping_plane_distance, far_clipping_plane_distance):
    gluPerspective(fov, aspect_ratio, near_clipping_plane_distance, far_clipping_plane_distance)


def draw_polygon(polygon):
    begin_polygon()
    for point in polygon.point_list:
        vertex_3fv(point.as_tuple())
    end()
