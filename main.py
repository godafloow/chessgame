import sys, pygame
import screeninfo as sc
from objects import *

pygame.init()

image = pygame.image.load(king.icon)
image_rect = image.get_rect()


for m in sc.get_monitors():
    if m.is_primary == True:
        height = m.height//1.5
        width = m.width//1.5


black = 0, 0, 0

screen = pygame.display.set_mode((width, height))

while True:
    #Exit Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    screen.fill(black)
    screen.blit(image, image_rect)
    pygame.display.flip()