from turtle_game import *
from random import *

bgcolor("black")
hideturtle()
width = window_width()
height = window_height()
speed(0)

def color_picker():
    num = randint(0,10)
    random_color = "white"
    if num == 0:
        random_color = "red"
    if num%2 == 0:
        random_color = "green"
    if num%3 == 0:
        random_color = "blue"
    if num%5 == 0:
        random_color = "yellow"

    return random_color


def draw_moon(xpos, ypos, moon_size, moon_color):
    penup()
    goto(xpos, ypos)
    pendown()

    dot(moon_size , moon_color)

def draw_star(xpos, ypos, size):
    penup()
    goto(xpos, ypos)
    pendown()

    dot(size, "white")

#for moon
moon_x = randrange(30, (width // 2))
moon_y = randrange(30, (height // 2))
moon_s = randrange(30, 50)
moon_c= color_picker()
draw_moon(moon_x, moon_y, moon_s, moon_c)

for i in range(100):
    x = randrange((-width // 2), (width // 2))
    y = randrange((-height // 2), (height // 2))
    draw_star(x, y, randrange(2, 12))

print("all starts have been drawn")
done()