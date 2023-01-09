#mports necessarios
import pygame, sys
from pygame.locals import *
import random
pygame.init()

#Cores
color_shade = (170,170,170)
color_dark = (100,100,100)
WHITE=(255,255,255)
RED=(255,0,0)
FORESTGREEN=(34,139,34)
WATERBLUE=(65,105,225)
#font usada nos butões e Logo em Menu/gameover /// e textos e respetivos descrições
smallfont = pygame.font.SysFont("Corbel",45,True)
gmfont=pygame.font.SysFont("Corbel",75,True)
smallgmfont = pygame.font.SysFont("Corbel",60,True)
textHO = smallfont.render("Heavy Ordnance" , True , WHITE)
textstart = smallfont.render("Start" , True , RED)
textquit = smallfont.render("Quit" , True , RED)

textgameover = gmfont.render("Game Over" , True , RED)
textpont = smallgmfont.render("Points: " , True , RED)
textname = smallgmfont.render("Name: " , True , RED)

#coordenadas dos butões
start_but=pygame.Rect(290,200,190,70)
exit_but=pygame.Rect(550,200,190,70)    