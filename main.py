import sys, pygame
from objects import *
from functions.buttonFunctions import *
from pygame import *
from functions.movementFunctions import *
from functions.gridFunctions import *

"""
TODO: FIX movement() IN objects.py (NEEDS TO WORK LIKE A ONE TIME BUTTON)
"""




#Initilizazing Pygame, Getting Screen Size, Cretaing a Display With Screen Size and setting up a clock
pygame.init()
width, height = getSize()[0], getSize()[1]
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Color for debugging
brown = 165, 42, 42
white = 127, 127, 127



#Default Rect
rectTest = Rect((270, 180), (width//8, height//8))


#We create the object king
king = King(rectTest)

while True:
    #Exit Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    
    
    #Clicker Test
    if clickButton(king.rect):
        screen.fill(white)
    else:
        screen.fill(brown)
    
    king.movement()
    #print(king.rectConverted, getSurRect(king.rectConverted))
    #print(detRectCliked())

    

    #Draws the lines of  the board
    for i in range(7):
        draw.line(screen, "white", ((i+1)*width//8,0), ((i+1)*width//8,height), 5)
        draw.line(screen, "white", (0, (i+1)*width//8), (height, (i+1)*width//8), 5)
    
    #Puts image of the object in the screen
    screen.blit(king.icon, king.rect)
    
    #Renders The Graphics
    pygame.display.flip()

    #Sets FPS to 60
    clock.tick(60)