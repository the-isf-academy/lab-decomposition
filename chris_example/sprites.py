from turtle import *


def pacman(radius, color, starting_ang, angle):
    # Draws Pac Man as the next 3 stages of it opening its mouth
    # Radius = Pacman's size
    # Color = Pacman's color"
    # Starting_ang = The angle that Pac Man starts with to keep the direction of the Pac Mans consistent when changed
    # Angle = The angle of the semi circle

    pencolor('black')
    setheading(0)
    left(starting_ang)
    forward(radius)
    fillcolor(color)
    begin_fill()
    left(90)
    circle(radius, angle)
    left(90)
    forward(radius)
    end_fill()


def bigfood(radius):
    # Draws the power up food that Pac Man eats
    # Radius = size of the circle

    color("black")
    fillcolor("white")
    begin_fill()
    circle(radius*0.7)
    end_fill()

