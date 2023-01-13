# player program

import sys, pygame, math
from pygame.locals import *

# set up a bunch of constants
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)
BROWN    = (139,  69,  19)
DARKGRAY = (128, 128, 128)

WINDOWWIDTH = 1000 # width of the program's window, in pixels
WINDOWHEIGHT = 380 # height in pixels

FPS = 60

# standard pygame setup code
pygame.init()
FPSCLOCK = pygame.time.Clock()
Window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Mini Projeto 3")

# draw the base cannon image
cannonIm = pygame.image.load("sprites/Cannon.png")
# draw the base background image
Background = pygame.image.load("sprites/Background.png").convert()
# draw the base projectile image
ProjectileIm = pygame.image.load("sprites/projectile.png")

def getAngle(x1, y1, x2, y2):
    # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
    rise = y1 - y2
    run = x1 - x2
    angle = math.atan2(run, rise) # get the angle in radians
    angle = angle * (180 / math.pi) # convert to degrees
    angle = (angle + 90) % 360 # adjust for a right-facing sprite
    return angle

# Initial projectile list
bullets = []

bullet_holdoff = 0

# Main application loop
while True:
    # Event to quit
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and pygame.key.get_pressed == K_ESCAPE):
            pygame.quit()
            sys.exit()

    cannonIm.blit(Window, (40, 245))
    Window.blit(Background, (0, 0))

    # Draw cannons pointed at the mouse cursor
    mousex, mousey = pygame.mouse.get_pos()
    for cannonx, cannony in ((40, 245), (40, 245)): #n sei pq mas so desenha se meter pelo menos 2 canhoes

        degrees = getAngle(cannonx, cannony, mousex, mousey)

        # rotate a copy of the cannon image and draw it
        rotatedSurf = pygame.transform.rotate(cannonIm, degrees)
        rotatedRect = rotatedSurf.get_rect()
        rotatedRect.center = (cannonx, cannony)
        Window.blit(rotatedSurf, rotatedRect)

    if pygame.mouse.get_pressed()[0]:
        bullet.angle = cannonIm.angle
        bullet.x = cannonIm.x
        bullet.y = cannonIm.y
        bullets.append(bullet)
    
    for bullet in bullets:
        bullet.draw()

    for bullet in bullets:
        if bullet.angle == 0:
            bullet.x = bullet.x + 5
        elif bullet.angle == 90:
            bullet.y = bullet.y - 5
        elif bullet.angle == 180:
            bullet.x = bullet.x - 5
        elif bullet.angle == 270:
            bullet.y = bullet.y + 5

    if bullet_holdoff == 0:
        if pygame.mouse.get_pressed()[0]:
            bullet.angle = cannonIm.angle
            bullet.x = cannonIm.x
            bullet.y = cannonIm.y
            bullets.append(bullet)
            bullet_holdoff = 100
    else:
        bullet_holdoff = bullet_holdoff - 1

    pygame.display.update()
    FPSCLOCK.tick(FPS)