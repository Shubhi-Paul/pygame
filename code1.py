import pygame
import time
import random

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

def playercar(x,y):
    gameDisplay.blit(player_car,(x,y))

def start_text():
    largetext = pygame.font.Font('freesansbold.ttf',25)
    textSurf = largetext.render("Press any key to begin the game !", True, red)
    textRect = textSurf.get_rect()
    textRect.center=((screen_width/2 , screen_ht/5))
    gameDisplay.blit(textSurf, textRect)
    


def gameLoop():

    x_player = screen_width * 0.45
    y_player = screen_ht * 0.8
    x_change,y_change = 0,0

    gameQuit = False

    while not gameQuit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_DOWN: 
                    y_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x_player += x_change
        y_player += y_change

        gameDisplay.fill(white)

        playercar(x_player,y_player)

        pygame.display.update()
        clock.tick(60)
       


gameLoop()
pygame.quit()
quit()

'''
enemy_car = pygame.image.load('racecar2.png')

def enemycar(x,y):
    gameDisplay.blit(enemy_car,(x,y))

y_enemy = screen_ht * 0.2 
x_change, y_change = 0 ,0
'''