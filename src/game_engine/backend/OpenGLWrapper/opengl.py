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


def draw_polygon(polygon, rgb_fill=None, rgb_outline=None, outline_thickness=None):
    __draw_fill(polygon, rgb_fill)
    if outline_thickness is not None:
        __draw_outline(polygon, rgb_outline, outline_thickness)


def __draw_fill(polygon, rgb):
    __set_fill_color(rgb)
    begin_polygon()
    for point in polygon.point_list:
        vertex_3fv(point.as_tuple())
    end()


def __draw_outline(polygon, rgb, thickness):
    __set_outline_color(rgb)
    glLineWidth(thickness)
    begin_polygon()
    for point in polygon.point_list:
        vertex_3fv(point.as_tuple())
    end()


def __set_fill_color(rgb):
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    if rgb:
        glColor3f(rgb.red, rgb.green, rgb.blue)
    else:
        glColor3f(1, 1, 1)


def __set_outline_color(rgb):
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    if rgb:
        glColor3f(rgb.red, rgb.green, rgb.blue)
    else:
        glColor3f(1, 1, 1)
