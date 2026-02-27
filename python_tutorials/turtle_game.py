from turtle import *
from random import *

speed(0)
turtle_speed = 10
game_over = False
bgcolor("#D2691E")
start_x = -50
start_y = 50

def draw_water():
    penup()
    goto(200, 450)
    pendown()
    color("blue")
    begin_fill()
    goto(1000, 450)
    goto(1000, -450)
    goto(200, -450)
    goto(200, 450)
    end_fill()

draw_water()

done()