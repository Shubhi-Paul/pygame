import pygame
import random
import time

pygame.init()

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Reflex Time")

red = (225,0,0)
blue = (0,0,225)
black =(0,0,0)

def gameloop():
    t=0
    gameExit = False

    while not gameExit :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
           
            if t == 2 and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] or mouse_presses[2] :
                    t1 = time.perf_counter() - t0
                    textfont = pygame.font.Font('freesansbold.ttf',35)
                    textSurf = textfont.render(". . .", True, black)
                    textRect = textSurf.get_rect() 
                    textRect.center = (400,270)
                    gameDisplay.blit(textSurf,textRect)

                    textfont2 = pygame.font.Font('freesansbold.ttf',20)
                    textSurf = textfont2.render("REACTION TIME : " + str(t1), True, black)
                    textRect = textSurf.get_rect() 
                    textRect.center = (400,310)
                    gameDisplay.blit(textSurf,textRect)
                    pygame.display.update()
                    t+=1
                    time.sleep(3)
                    pygame.quit()
                    quit()
                    
            if t == 0:
                gameDisplay.fill(red)

                textfont = pygame.font.Font('freesansbold.ttf',35)
                textSurf = textfont.render("CHECK YOUR REFLEXES", True, black)
                textRect = textSurf.get_rect() 
                textRect.center = (400,270)
                gameDisplay.blit(textSurf,textRect)

                textfont2 = pygame.font.Font('freesansbold.ttf',20)
                textSurf = textfont2.render("WHEN THE SCREEN TURNS BLUE, CLICK AS QUICKLY AS YOU CAN !!", True, black)
                textRect = textSurf.get_rect() 
                textRect.center = (400,310)
                gameDisplay.blit(textSurf,textRect)

                textSurf = textfont2.render("CLICK ANYWHERE TO START", True, black)
                textRect = textSurf.get_rect() 
                textRect.center = (400,340)
                gameDisplay.blit(textSurf,textRect)

                textSurf = textfont2.render(". . . . . . .", True, black)
                textRect = textSurf.get_rect() 
                textRect.center = (400,360)
                gameDisplay.blit(textSurf,textRect)
                pygame.display.update()
                t+=1

            if t == 1 and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0] or mouse_presses[2] :
                    gameDisplay.fill(red) 
                    textfont = pygame.font.Font('freesansbold.ttf',35)
                    textSurf = textfont.render(". . .", True, black)
                    textRect = textSurf.get_rect() 
                    textRect.center = (400,270)
                    gameDisplay.blit(textSurf,textRect)

                    textfont2 = pygame.font.Font('freesansbold.ttf',20)
                    textSurf = textfont2.render("WAIT FOR BLUE", True, black)
                    textRect = textSurf.get_rect() 
                    textRect.center = (400,310)
                    gameDisplay.blit(textSurf,textRect)
                    pygame.display.update()
            
                    sec = random.randrange(2,4)
                    time.sleep(sec)
                    gameDisplay.fill(blue)
                    pygame.display.update()
                    t0 = time.perf_counter()
                    t +=1          
        
        clock.tick(60)
    
gameloop()
