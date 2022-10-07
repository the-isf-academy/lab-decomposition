############################################################
# This is an adapted version of a previous student's work
############################################################


from turtle import *
from sprites import pacman,  bigfood
from helpers import no_delay, setup_custom
from background import background
import time
import settings

def draw_animation_pacman(num_frames, sleeptime, paccolor):
    #The full animation of Pac Man moving on the map

    for i in range(num_frames):
        with no_delay():
            clear()
            background()
            
            # draws the power up food on the screen, until the pacman has moved past it
            if i < 36:
                setup_custom(240, -35)
                bigfood(50) 

            # sets the initial position of the pacman
            # changes the x cordinate each from to move the pacman
            setup_custom(-120+(10*i),0)

            # draws the pacman 
            pacman(50, paccolor, 25, 310)
            
        # time between frames
        time.sleep(sleeptime)


def main():
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
    bgcolor('black')

    for i in range(settings.NUMREPEATS):
        draw_animation_pacman(settings.NUMFRAMES, settings.SLEEPTIME, settings.PACCOLOR)
    
    input("Press enter to exit...")

main()