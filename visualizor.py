import pyglet
from pyglet.gl import *
from pyglet.window import key
import csv

WINDOW = 400
INCREMENT = 1


def load_data(filename: str) -> [(float, float, float, float, float, float)]:
    reader = csv.reader(open(filename, "r"))
    result = []
    for row in reader:
        result.append(tuple(float(x)*20 for x in row))
    return result


class Window(pyglet.window.Window):
    # Cube 3D start rotation
    xRotation = yRotation = 30
    focus = 35
    aspectRatio = 1

    def __init__(self, width, height, title=''):
        super(Window, self).__init__(width, height, title, resizable=True)
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)

    def on_draw(self):
        # Clear the current GL Window
        self.clear()

        # Push Matrix onto stack
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0)
        glRotatef(self.yRotation, 0, 1, 0)

        glLineWidth(1.5)
        # Draw the six sides of the cube

        glBegin(GL_LINES)
        glColor3f(1, 0, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(20, 0, 0)

        glColor3f(0, 1, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 20, 0)

        glColor3f(0.25, 0.5, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 20)
        glEnd()

        glBegin(GL_LINES)
        for row in lines:
            glColor3f(1, 1, 1)
            glVertex3d(row[0], row[1], row[2])
            glVertex3d(row[3], row[4], row[5])
        glEnd()

        # Pop Matrix off stack
        glPopMatrix()

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.focus, self.aspectRatio, 1, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -400)

    def on_resize(self, width, height):
        # set the Viewport
        glViewport(0, 0, width, height)

        # using Projection mode
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        self.aspectRatio = width / height
        gluPerspective(self.focus, self.aspectRatio, 1, 1000)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, 0, -400)

    def on_text_motion(self, motion):
        if motion == key.UP:
            self.xRotation -= INCREMENT
        elif motion == key.DOWN:
            self.xRotation += INCREMENT
        elif motion == key.LEFT:
            self.yRotation -= INCREMENT
        elif motion == key.RIGHT:
            self.yRotation += INCREMENT
        elif motion == key.PAGEUP:
            self.focus -= 0.3
        elif motion == key.PAGEDOWN:
            self.focus += 0.3


if __name__ == '__main__':
    lines = load_data("vis.csv")
    Window(WINDOW, WINDOW, 'Jet 3D visualizer')
    pyglet.app.run()
