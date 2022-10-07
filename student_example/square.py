from turtle import *
from movement import no_delay
from time import sleep


def basic_square(square_size, square_color):
    # This function draws a basic square with no delay 
    # It can draw a square of any color and any size

    with no_delay():
        fillcolor(square_color)
        pencolor(square_color)

        begin_fill()
        for i in range(4):
            forward(square_size)
            right(90)

        end_fill()

