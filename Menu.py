from Imports import *
SCREEN=pygame.display.set_mode((1000,380))
SCREEN.fill((0,0,0))

def menuini():

    while True:  
        for event in pygame.event.get():
                            #posição do constante mouse    
            if event.type==pygame.MOUSEMOTION:
                #posição do mouse    
                pos=pygame.mouse.get_pos()    
                                    

                                    #start button
                if start_but.collidepoint(pos):
                    #butão start e o "blit" "acende" o butão quando o rato passa por cima
                    pygame.draw.rect(SCREEN,WHITE,(290,200,190,70))
                    SCREEN.blit(textstart,(330,210))
                    pygame.display.update()
                    #se o butão for carregado
                    if pygame.mouse.get_pressed()[0] and start_but.collidepoint(pos):
                        print("Move on")
                        #provavelmente não a melhor maneira de passar pra outro screen mas foi oque deu
                        from Gamefile import SCREENGAME
                
                                                      
                                            
                #exit button
                if exit_but.collidepoint(pos):
                    #butão start e o "blit" "acende" o butão quando o rato passa por cima
                    SCREEN.blit(textquit,(550,200))
                    pygame.draw.rect(SCREEN,WHITE,(550,200,190,70))
                    pygame.display.update()
                    #se o butão for carregado
                    if pygame.mouse.get_pressed()[0] and exit_but.collidepoint(pos):
                        SCREEN.blit(textquit,(590,210))
                        #sai do jogo
                        print("quit")
                        pygame.quit()   
                        sys.exit()
        SCREEN.fill((0,0,0))            
        SCREEN.blit(textHO,(310,80))

        #startbutton default sem interferencia do MOUSE
        pygame.draw.rect(SCREEN,color_shade,(290,200,190,70))
        #highlight text
        SCREEN.blit(textstart,(330,210))

        #exitbut default sem interferencia do MOUSE
        pygame.draw.rect(SCREEN,color_shade,(550,200,190,70))
        #highlight text
        SCREEN.blit(textquit,(590,210))             
                    
        pygame.display.update()            

menuini()