#Imports de ficheiro "Imports" que guarda classes, cores, etc
from Imports import *
SCREEN=pygame.display.set_mode((1000,380))
SCREEN.fill((0,0,0))

font = pygame.font.SysFont(None, 100)

input_active = True

def gameoverfunc():
    text = ""
    SCREEN.fill((0,0,0))
    while True: 
         
        for event in pygame.event.get():
                #posição do constante mouse    
                if event.type==pygame.MOUSEMOTION:
                    #posição do mouse    
                    pos=pygame.mouse.get_pos()
                    
                #deteta tecla pressionada e escreve-a na textbox    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    input_active = True
                    text = ""
                elif event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text =  text[:-1]
                    else:
                        text += event.unicode
                
                    
        text_surf = font.render(text, False, (255, 0, 0))
       
        pygame.draw.rect(SCREEN,(0,0,0),(525,220,500,70))
        pygame.draw.rect(SCREEN,color_shade,(525,220,190,70)) 
        SCREEN.blit(text_surf,(530,220))
        pygame.display.flip()
        
       
                    
        SCREEN.blit(textgameover,(360,60))
        #texto de Pontuação do jogador
        SCREEN.blit(textpont,(390,150))
        SCREEN.blit(textname,(390,220))
        #highlight text
        #SCREEN.blit(textstart,(330,210))
        
         

        
        pygame.display.update()

gameoverfunc()