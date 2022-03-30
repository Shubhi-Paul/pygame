import pygame
import time
import random

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

def enemy(x,y,w,h):
    pygame.draw.rect(gameDisplay,red,[x,y,w,h]) 
    

def display_text(text):
    """
    display text in the game window
    """
    largeText = pygame.font.Font('freesansbold.ttf',55)
    textSurface = largeText.render(text,True,red)
    textRect = textSurface.get_rect()
    textRect.center = (display_width/2,display_height/5)
    gameDisplay.blit(textSurface, textRect)
    pygame.display.update()

def display_text2(text):
    """
    display text in the game window
    """
    smallText = pygame.font.Font('freesansbold.ttf',35)
    textSurface = smallText.render(text,True,red)
    textRect = textSurface.get_rect()
    textRect.center = (display_width/2,display_height/4 + 20)
    gameDisplay.blit(textSurface, textRect)
    pygame.display.update()

def gameOver(score):
    """
    display GAME OVER message when car touches the edge
    """
    display_text ("GAME OVER")
    display_text2("Score : " + str(score)) 
    
    time.sleep(2)
    game_loop()

    


def crash():
    """
    display CRASH message when car touches the edge
    """
    display_text ("YOU CRASHED")
    #display_text(str(x))
    time.sleep(2)
    game_loop()

def display_shape():
    pygame.draw.rect(gameDisplay, red, [40,50,160,70])

def disp_dodged(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged : "+str(score),True,black)
    gameDisplay.blit(text,(10,10))


def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    car_width = 75
    car_height = 90

    score=0

    x_enemy = random.randint(0,display_width-75)
    y_enemy= 0
    enemy_width = 60
    enemy_height = 60
    speed_enemy = 5

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
            
        x += x_change
        y += y_change 

        gameDisplay.fill(white)
        #display_text("where is my car?")
        #display_text(str(x))
        enemy(x_enemy,y_enemy,enemy_width,enemy_height)
        y_enemy += speed_enemy
        if y_enemy > display_height:
            y_enemy = 0
            x_enemy = random.randint(0,display_width-75)
            score +=1
            if speed_enemy < 17:
                speed_enemy += 1
                enemy_width += 7

        car(x,y)
        disp_dodged(score)
        
        if x > display_width - car_width or x < 0:
            crash()
        if y > display_height - car_height :
            if event.key == pygame.K_DOWN:
                    y_change = 0        
        elif y < 3: 
            if event.key == pygame.K_UP:
                    y_change = 0

        if y >= y_enemy - car_height and y <= y_enemy + enemy_height:    
            if x>= x_enemy and x <= x_enemy + enemy_width or x + car_width >= x_enemy and x + car_width <= x_enemy + enemy_width:
                gameOver(int(score))
   
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
