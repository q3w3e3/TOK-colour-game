import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import Window
import math
import random

window = pyglet.window.Window(caption='TOK GAME', resizable=True)

pyglet.gl.glClearColor(1, 1, 1, 1)

space = 0

def circle(x, y, radius, g, b):
    iterations = 8
    s = math.sin(2*math.pi / iterations)
    c = math.cos(2*math.pi / iterations)
    dx, dy = radius, 0
 
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,g,b)
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
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,  ('v2f', ((window.width//2.1),(window.height//2),(window.width//1.9),(window.height//2))), ('c3i', (0,0,0)*2))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,  ('v2f', ((window.width//2),((window.height//2)+(window.width//40)),(window.width//2),((window.height//2)-(window.width//40)))), ('c3i', (0,0,0)*2))

@window.event
def on_key_press(symbol, modifiers):
    window.clear()
    global space
    g = random.uniform(0.1,1)
    b = random.uniform(0.1,1)
    if symbol == key.F:
        window.set_fullscreen(fullscreen=True, screen=None)
    if symbol == key.BACKSPACE:
        window.clear()
    if symbol == key.SPACE:
        space = space+1
        for a in xrange (0,360,30):
            circle((math.sin(math.radians(a))*(window.height//2.5))+(window.width//2),(math.cos(math.radians(a))*(window.height//2.5))+(window.height//2),window.height//12,g,b)
        r = random.randrange(0,360,30)
        print r,'degrees'
        circle((math.sin(math.radians(r))*(window.height//2.5))+(window.width//2),(math.cos(math.radians(r))*(window.height//2.5))+(window.height//2),window.height//12,(g+(1-(random.gauss(0,1)))),(b+(1-(random.gauss(0,1)))))
pyglet.app.run()
