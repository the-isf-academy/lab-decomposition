# Helpers
# By Chris Proctor
# ----------------
# A mishmash of useful functions. Feel free to use these in your own projects if they are helpful to you.

from turtle import *
from itertools import chain, cycle

def setup_custom(x, y):
    '''Sets up the turtle, ready to draw,
    at the given coordinates'''
    penup()
    goto(x,y)
    pendown()
    speed(0)
    hideturtle()
    setheading(0)
    tracer(0)



class no_delay:
    "A context manager which causes drawing code to run instantly"

    def __enter__(self):
        self.n = tracer()
        self.delay = delay()
        tracer(0, 0)

    def __exit__(self, exc_type, exc_value, traceback):
        update()
        tracer(self.n, self.delay)
