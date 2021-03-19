#Modificaciones:
#   -Agrega contador de taps
#   -Notifica cuando se completa el juego
#   -Digito centrado al cuadro
from random import shuffle
from turtle import Turtle, up, goto, down, color,\
    begin_fill, forward, left, end_fill, update, \
    ontimer, clear, shape, stamp, write, setup,\
    hideturtle, tracer, listen, addshape, onscreenclick,\
    done
from freegames import path
import time


car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
writer = Turtle(visible=False)
counter = {'contador': 0}
find = {'encontrados': 0}


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    counter['contador'] += 1
    writer.undo()
    writer.write(counter['contador'])

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        find['encontrados'] += 2
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        if find['encontrados'] == 64:
            update()
            ontimer(draw, 100)
            writer.goto(50, 200)
            writer.color('green')
            writer.write("GAME OVER")
            time.sleep(5)
            quit()


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        if (tiles[mark] < 10):
            goto(x + 14, y + 2)
        elif (tiles[mark] < 20):
            goto(x + 2, y + 2)
        else:
            goto(x + 4, y + 2)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 440, 370, 0)
hideturtle()
tracer(False)
writer.goto(0, 200)
writer.color('green')
writer.write(counter['contador'])
listen()
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
