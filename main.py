import sys, pygame
from objects import *
from functions.buttonFunctions import *
from pygame import *


pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

brown = 165, 42, 42

king = King()


while True:
    #Exit Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    
    if clickButton(king.rect):
        screen.fill(brown)
    else:
        screen.fill(brown)
    
    screen.blit(king.icon, king.rect)
    
    for i in range(7):
        draw.line(screen, "white", ((i+1)*width//8,0), ((i+1)*width//8,height), 5)
        draw.line(screen, "white", (0, (i+1)*width//8), (height, (i+1)*width//8), 5)
    
    pygame.display.flip()
    clock.tick(60)