from turtle import *
from helpers import setup_custom

#Pieces to make the maze

def rectangle(side_length):
    # Draws a repeated piece of the Pac Man maze"
    right(90)
    forward(side_length)
    right(90)

def rectangle2(side_length2):
    # Draws a repeated piece of the Pac Man maze"

    left(90)
    forward(side_length2)
    left(90)

def background():
    # Draws the Pac Man maze"

    pensize(3)
    color("blue")

    setup_custom(-320, 60)


    forward(200)
    rectangle2(105)
    forward(200)
    rectangle(120)
    forward(200)
    left(90)
    forward(400)
    rectangle(120)
    forward(400)
    left(90)
    forward(360)
    rectangle(120)
    forward(360)
    rectangle2(105)
    forward(360)
    rectangle(120)
    forward(200)
    left(90)
    forward(300)
    rectangle(120)
    forward(300)
    left(90)
    forward(180)
    left(90)
    forward(300)
    rectangle(120)
    forward(300)
    left(90)
    forward(60)
    right(90)
    forward(120)
