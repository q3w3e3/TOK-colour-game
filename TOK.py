import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import Window
import math
import random

window = pyglet.window.Window(caption='TOK GAME', resizable=True, style=Window.WINDOW_STYLE_DIALOG)

pyglet.gl.glClearColor(1, 1, 1, 1)

space = 1


def circle(x, y, radius, r, g, b):
    iterations = int(2*math.pi*radius)
    s = math.sin(2*math.pi / iterations)
    c = math.cos(2*math.pi / iterations)
    dx, dy = radius, 0
 
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(r,g,b)
    glVertex2f(x, y)
    for i in range(iterations+1):
        glVertex2f(x+dx, y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    glEnd()
    
@window.event
def on_activate():
    window.clear()

@window.event
def on_resize(width, height):
    window.clear()
@window.event
def on_draw():
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,  ('v2f', (((window.width//2)+(window.height//40)),(window.height//2),((window.width//2)-(window.height//40)),(window.height//2))), ('c3i', (0,0,0)*2))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,  ('v2f', ((window.width//2),(window.height//2.1),(window.width//2),(window.height//1.9))), ('c3i', (0,0,0)*2))

@window.event
def on_key_press(symbol, modifiers):
    global space
    r = math.fabs(random.gauss(0,0.25))
    g = random.uniform(0.2,1)
    b = random.uniform(0.2,1)
    gr = 2*(random.gauss(0,space**-1))
    br = 2*(random.gauss(0,space**-1))
    sign = random.choice([-1,1])
    if symbol == key.F:
        if window.fullscreen == True:
            window.set_fullscreen(fullscreen=False, screen=None)
        elif window.fullscreen == False:
            window.set_fullscreen(fullscreen=True, screen=None)
    if symbol == key.BACKSPACE:
        window.clear()
    if symbol == key.SPACE:
        window.clear()
        space = space+1
        for a in xrange (0,360,30):
            circle((math.sin(math.radians(a))*(window.height//2.5))+(window.width//2),(math.cos(math.radians(a))*(window.height//2.5))+(window.height//2),window.height//12,r,g,b)
        c = random.randrange(0,360,30)
        print c, 'degrees'
        circle((math.sin(math.radians(c))*(window.height//2.5))+(window.width//2),(math.cos(math.radians(c))*(window.height//2.5))+(window.height//2),window.height//12,r,g+(sign*gr),b+(sign*br))
pyglet.app.run()
