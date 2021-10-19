import pygame
import time

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Shubhi's Game Version 1")

#color_______________________

black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)

clock = pygame.time.Clock()

car_player = pygame.image.load('images//racecar.png')
car_enemy = pygame.image.load('images//racecar2.png')

def car(x,y):
    gameDisplay.blit(car_player,(x,y))

def display_text(text):
    largeText = pygame.font.Font('freesansbold.ttf',85)
    textSurface = largeText.render(text,True,black)
    textRect = textSurface.get_rect()
    textRect.center = (display_width/2,display_height/2)
    gameDisplay.blit(textSurface, textRect)
    pygame.display.update()

def display_shape():
    pygame.draw.rect(gameDisplay, red, [40,50,160,70])

def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    car_width = 73
    car_heigth = 50

    x_change = 0
    y_change = 0

    gameExit = False
    while not gameExit:
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
            else:
                x_change,y_change=0,0
            '''
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0'''
        x += x_change
        y += y_change 

        gameDisplay.fill(white)
        #display_text("where is my car?")
        car(x,y)
        

        #if x > display_width - car_width or x < 0:
            # display "crash"
        #if y > display_height - car_height or y < 0:
            # display "crash"

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()