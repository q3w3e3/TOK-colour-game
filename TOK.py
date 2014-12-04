import pyglet

from pyglet.gl import *

import math

import random

from pyglet import clock

window = pyglet.window.Window(resizable=True)

from pyglet.window import key
from pyglet.window import Window

@window.event

def circle(x, y, radius):
    iterations = int(2*radius*math.pi)
    s = math.sin(2*math.pi / iterations)
    c = math.cos(2*math.pi / iterations)
    g = random.uniform(0.1,1)
    b = random.uniform(0.1,1)
    dx, dy = radius, 0
 
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,g,b)
    glVertex2f(x, y)
    for i in range(iterations+1):
        glVertex2f(x+dx, y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    glEnd()
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.BACKSPACE:
        window.clear()
    if symbol == key.SPACE:
        circle(window.width//2,window.height//2,(window.height//12)//2)
pyglet.app.run()
