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
from turtle import up, goto, down, begin_fill, \
    forward, left, end_fill, onkey, done, setup,\
    onscreenclick, listen, undo, clear,\
    fillcolor
import math
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
    radius = ((end.x - start.x)*(end.x - start.x))
    radius = radius + ((end.y - start.y)*(end.y - start.y))
    radius = math.sqrt(radius)
    t.circle(radius)
    end_fill()


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
    up()
    goto(start.x, start.y)
    down()
    turtle.penup()
    turtle.setpos(start.x, start.y)
    turtle.pendown()
    for i in range(5):
        turtle.forward(200)
        turtle.right(144)


def covid(start, end):
    up()
    goto(start.x, start.y)
    down()
    fillcolor('green')
    begin_fill()
    contador = 0
    while True:
        forward(end.x - start.x)
        left(170)
        contador = contador + 1
        if contador > 36:
            break
    end_fill()


color = None
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
onkey(lambda: color('pink'), 'P')  # nuevo color
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('shape', star), 'e')
onkey(lambda: store('shape', covid), 'p')
onkey(clear, 'b')
done()
