#mports necessarios
import pygame, sys
from Imports import *
SCREENGAME=pygame.display.set_mode((1000,380))
SCREENGAME.fill((0,0,0))

class GameObject():
    
    def __init__(self):
        self.gObjects = []
        self.gObjects.append(object)
        print(self.gObjects)
    
    def draw(self):
        for o in self.gObjects:
           pygame.draw.rect(SCREENGAME,RED,(smallship.x,smallship.y,30,30))
           #pygame.draw.rect(SCREENGAME,RED,(smallship.x1,smallship.y1,30,30))
           #pygame.draw.rect(SCREENGAME,RED,(smallship.x2,smallship.y2,30,30))
           #pygame.draw.rect(SCREENGAME,RED,(smallship.x3,smallship.y3,30,30))
           
    
class ship(GameObject):
    vel=0.03

    x=1100
    y=340

    #x1=1200
    #y1=340

    #x2=1350
    #y2=340

    #x3=1450
    #y3=340

    hp=100

    def __init__(self, hp, vel):
        self.hp = hp
        self.vel = vel
        #self.type = 

    def update(self):
        ship.x -= self.vel
        #ship.x1 -= self.vel
        #ship.x2 -= self.vel
        #ship.x3 -= self.vel
       
class smallship(ship):    
    def __init__(self, hp, vel, size):
        self.size = size
        
        
gameObj = GameObject()
shipupdate = ship(ship.hp,ship.vel)

while True:  
        for event in pygame.event.get():
            #posição do constante mouse    
            if event.type==pygame.MOUSEMOTION:
                    #posição do mouse    
                    pos=pygame.mouse.get_pos()
                    
        SCREENGAME.fill((0,191,255))
        
        #canhão
        pygame.draw.rect(SCREENGAME,color_shade,(40,220,10,30))
        #plataforma do jogador
        pygame.draw.rect(SCREENGAME,color_dark,(30,240,30,10))
        #zona de spawn do jogador
        pygame.draw.rect(SCREENGAME,FORESTGREEN,(0,250,120,200))
        #dangerzone
        n1=pygame.draw.rect(SCREENGAME,RED,(120,360,120,100))
        
        
        #agua
        pygame.draw.rect(SCREENGAME,WATERBLUE,(240,360,780,100))  
         
        #se tocar na dangerzone desaparece
        #if n1[0]>=n2[0]:
        #   print("dead")
        

        gameObj.draw()
        shipupdate.update()
        
        pygame.display.update()