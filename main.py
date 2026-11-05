import sys, pygame
import screeninfo as sc
from objects import *
from functions.buttonFunctions import *

pygame.init()

for m in sc.get_monitors():
    if m.is_primary == True:
        height = m.height//1.5
        width = m.width//1.5


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

kingicon = pygame.image.load(king.icon).convert()
kingicon = pygame.transform.scale(kingicon, (128,128))
king_rect = kingicon.get_rect()

while True:
    #Exit Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    if clickButton(king_rect):
        screen.fill("white")
    else:
        screen.fill("black")
    
    
    screen.blit(kingicon, king_rect)
    pygame.display.flip()
    clock.tick(60)