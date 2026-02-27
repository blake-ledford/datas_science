from turtle import *

diameter = 40 #pixels
pop_diamter = 100 #pixels

def draw_balloon ():
    color("red")
    dot(diameter)

def inflate_balloon ():
    global diameter #gives access to vars in global scope
    diameter = diameter + 10
    draw_balloon()

    if diameter >= pop_diamter:
        clear()
        diameter = 40
        write("Pop!")

draw_balloon() #function call

onkey(inflate_balloon, "space")
listen()
#finish turtle commands
done()