#mports necessarios
import pygame, sys
from Imports import *
SCREENGAME=pygame.display.set_mode((1000,380))
SCREENGAME.fill((0,0,0))

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
        #ship
        #970 320
        n2=pygame.draw.rect(SCREENGAME,RED,(ships.x,ships.y,30,30))
        
        
         
        #se tocar na dangerzone desaparece
        if n1[0]>=n2[0]:
            print("dead")

        pygame.display.update()