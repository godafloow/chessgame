import sys, pygame
import screeninfo as sc
from objects import *

pygame.init()

kingicon = pygame.image.load(king.icon)
king_rect = kingicon.get_rect()

queenicon = pygame.image.load(queen.icon)
queen_rect = kingicon.get_rect()


for m in sc.get_monitors():
    if m.is_primary == True:
        height = m.height//1.5
        width = m.width//1.5

queenicon = pygame.transform.scale(queenicon, (128, 128))
kingicon = pygame.transform.scale(kingicon, (128,128))
black = 0, 0, 0

screen = pygame.display.set_mode((width, height))

while True:
    #Exit Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    screen.fill(black)
    screen.blit(queenicon, (width/2, height/2))
    screen.blit(kingicon, king_rect)
    pygame.display.flip()