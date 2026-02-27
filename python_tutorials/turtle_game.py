from turtle import *
from random import *

speed(0)
turtle_speed = 50
game_over = False
bgcolor("#D2691E")
start_x = -500
start_y = 0

def draw_water():
    penup()
    goto(300, 450)
    pendown()
    color("blue")
    begin_fill()
    goto(1000, 450)
    goto(1000, -450)
    goto(300, -450)
    goto(300, 450)
    end_fill()

draw_water()

penup()
goto(start_x, start_y)
shape("turtle")
color("green")

def move_up():
    setheading(90)
    forward(turtle_speed)
    check_goal()

def move_right():
    setheading(0)
    forward(turtle_speed)
    check_goal()

def move_left():
    setheading(180)
    forward(turtle_speed)
    check_goal()

def move_down():
    setheading(270)
    forward(turtle_speed)
    check_goal()

def check_goal():
    global game_over
    if xcor() > 300:
        hideturtle()
        color("white")
        write("YOU WIN!")

        onkey(None, "Up")
        onkey(None, "Right")
        onkey(None, "Down")
        onkey(None, "Left")

        onkey(None, "w")
        onkey(None, "d")
        onkey(None, "a")
        onkey(None, "s")

onkey(move_up, "Up")
onkey(move_right, "Right")
onkey(move_down, "Down")
onkey(move_left, "Left")

onkey(move_up, "w")
onkey(move_right, "d")
onkey(move_left, "a")
onkey(move_down, "s")

listen()

done()