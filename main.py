import sys, pygame
from objects import *
from functions.buttonFunctions import *
from pygame import *
from functions.movementFunctions import *
from functions.gridFunctions import *


#Initilizazing Pygame, Getting Screen Size, Cretaing a Display With Screen Size and setting up a clock
pygame.init()
width, height = getSize()[0], getSize()[1]
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#Color for debugging
brown = 165, 42, 42


#Default Rect
rectTest = Rect((0, 0), (width//8, height//8))


#We create the object king
king = King()


while True:
    #Exit Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()    
    
    #Clicker Test
    if clickButton(king.rect):
        screen.fill(brown)
    else:
        screen.fill(brown)
    
    
    #Draws the lines of  the board
    for i in range(7):
        draw.line(screen, "white", ((i+1)*width//8,0), ((i+1)*width//8,height), 5)
        draw.line(screen, "white", (0, (i+1)*width//8), (height, (i+1)*width//8), 5)
    
    print(king.isCliked(rectTest))
    
    
    #Puts image of the object in the screen
    screen.blit(king.icon, rectTest)
    
    #Renders The Graphics
    pygame.display.flip()
    

    #Sets FPS to 60
    clock.tick(60)