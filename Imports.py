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
#font usada nos butões e Logo em Menu /// e textos e respetivos descrições
smallfont = pygame.font.SysFont("Corbel",45,True)
textHO = smallfont.render("Heavy Ordnance" , True , WHITE)
textstart = smallfont.render("Start" , True , RED)
textquit = smallfont.render("Quit" , True , RED)
#coordenadas dos butões
start_but=pygame.Rect(290,200,190,70)
exit_but=pygame.Rect(550,200,190,70)

class ships:
    x=400-0.1
    y=340
    hp=100
    def __init__(self,x,y,hp):
        print("houdy")
        self.x=x
        self.y=y
        self.hp=hp
  