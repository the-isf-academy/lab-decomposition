from turtle import *
from square import basic_square
import settings
from movement import fly
from time import sleep
from math import sqrt, pow

def draw_animation(num_squares, sleeptime):
    
    # keeps track of which number square is being drawn
    square_count = 0

    square_size = settings.square_size

    for i in range(num_squares):
      
        # by using the if statements, I can switch the fill color of each square,
        #and this creates my color pattern.

        if square_count%2 == 0:
            basic_square(square_size, settings.color1)
        else:
            basic_square(square_size, settings.color2)

        square_count = 1 + square_count

        # This effects the amount of in between each square
        sleep(sleeptime)
        
        # This rotates the pen so the squares draw inside of each other
        penup()
        forward(square_size/2)
        right(45)
        pendown()

        # This equation calculates the next size square to draw.
        # It is taken from the pythagorean theorem.
        # It is a^2 + b^2 = c^2 reversed, to decrease the square size so it fits
        # exactly inside the square bigger than it.
        square_size = sqrt((pow(square_size,2)/2))

       
    clear()
    setheading(0)


if __name__ == '__main__':
    screen = Screen()
    screen.setup(settings.screen_width,settings.screen_height)

    hideturtle()
    speed(0)

    # Loops the main animation 
    for i in range(settings.num_repeats):

        # Start at the right location for the size of the screen
        fly(-settings.screen_width/2,settings.screen_width/2)

        draw_animation(settings.num_squares, settings.sleep_time)






