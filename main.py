import sys, pygame
import screeninfo as sc

pygame.init()

for m in sc.get_monitors():
    if m.is_primary == True:
        height = m.height/2
        width = m.width/2


speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()