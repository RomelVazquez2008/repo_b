"""Paint, for drawing shapes.
#prueba de las ramas
Exercises
1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
import turtle
from turtle import *
import math
from math import sqrt
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    t = turtle.Turtle() 
    up()
    goto(start.x, start.y)
    
    begin_fill()
    radius = math.sqrt(((end.x - start.x)*(end.x - start.x))+((end.y - start.y)*(end.y - start.y)))
    t.circle(radius)
    down()
    goto(end.x, end.y)
    end_fill()

    #up()
    #goto(start.x, start.y)
    #down()
    #begin_fill()

    #for count in range(50):
     #   forward(end.x - start.x)
      #  left(7.2)

    #end_fill()
    ###################
    #up()
    #goto(start.x, start.y)
    
    #down()
    #goto(end.x, end.y)

    #radio=math.sqrt(((end.x - start.x)*(end.x - start.x))+((end.y - start.y)*(end.y - start.y))) 
    #turtle.circle(radio)
    


def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for i in range(3):
        forward(end.x - start.x)
        left(120)
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

def star(start, end):
    


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')   
onkey(lambda: color('red'), 'R')
onkey(lambda: color('pink'), 'P') #nuevo color
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()