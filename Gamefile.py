#mports necessarios
import pygame, sys
from Imports import *

SCREENGAME = pygame.display.set_mode((1000,380))


class GameObject():
    
    def __init__(self):
        self.gObjects = []
    
    def add(self, obj):
        lenght=len(self.gObjects)
        if lenght<4:
            self.gObjects.append(obj)
            #print(self.gObjects)
            print(self.gObjects)
        else:
            pass
    def destroy(self, index):
        self.gObjects.remove(index)

    def getGameObject(self):
        return self.gObjects

    def draw(self, myscreen):
        for i in self.gObjects:
            if isinstance(i, ship):
                i.update()
                pygame.draw.rect(myscreen,RED,(i.x,i.y, i.size, 30))
               
            
class ship():
    const_vel=0.5
    init_x=1100
    init_y=340

    def __init__(self, vel, size):
        self.x = ship.init_x
        self.y = ship.init_y
        self.size = size
        self.vel = vel
    
    def update(self):
        self.x -= self.vel

        #print(self.x)
        #ship.x1 -= self.vel
        #ship.x2 -= self.vel
        #ship.x3 -= self.vel
       



gameObj = GameObject()
shipupdate = ship(ship.const_vel, 30)

gameObj.add(shipupdate)

counter = 0
while True: 
    pygame.display.flip()
    
    for event in pygame.event.get():
        #posição do constante mouse    
        if event.type==pygame.MOUSEMOTION:
                #posição do mouse    
                pos=pygame.mouse.get_pos()
                
    SCREENGAME.fill((0,191,255))
    
    #agua
    pygame.draw.rect(SCREENGAME,WATERBLUE,(240,360,780,100))
    
    #canhão
    pygame.draw.rect(SCREENGAME,color_shade,(40,220,10,30))
    #plataforma do jogador
    pygame.draw.rect(SCREENGAME,color_dark,(30,240,30,10))
    #zona de spawn do jogador
    pygame.draw.rect(SCREENGAME,FORESTGREEN,(0,250,120,200))
    #dangerzone
    n1=pygame.draw.rect(SCREENGAME,RED,(120,360,120,100))

    #pygame.draw.rect(SCREENGAME,RED,(900, 340, 30, 30))

    gameObj.draw(SCREENGAME)

    #se tocar na dangerzone desaparece
    
    
    counter += 1
    if counter % 250 == 0:
        gameObj.add(ship(ship.const_vel,60))
    
    keys = pygame.key.get_pressed()     
    if keys[pygame.K_LEFT]:             
            gameObj.destroy()


    pygame.time.Clock().tick(60)