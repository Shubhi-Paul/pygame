import pygame
import time

pygame.init()

clock = pygame.time.Clock()

screen_width , screen_ht = 800 , 600
gameDisplay = pygame.display.set_mode((screen_width,screen_ht))
pygame.display.set_caption("trial code")

player_car =  pygame.image.load('racecar.png')

white = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
blue  = (0,0,255)
green = (0,255,0)

def car(x,y):
    gameDisplay.blit(player_car,(x,y))

def gameLoop():

    gameDisplay.fill(white)
    x = screen_width * 0.45
    y = screen_ht * 0.8

    gameQuit = False

    while not gameQuit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        car(x,y)
        pygame.display.update()
        clock.tick(60)
       


gameLoop()
pygame.quit()
quit()
