import pygame

pygame.init()

#color_scheme
white = (255,255,255)
black = (0,0,0)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(black)

def rect():
    #pygame.draw.rect(gameDisplay,color,[x,y,w,h])
    pygame.draw.rect(gameDisplay,red,[10,10,60,70])
    pygame.draw.rect(gameDisplay,blue,[100,30,70,70])

def circle():
    #pygame.draw.circle(gameDisplay,color,(x,y),radius)
    pygame.draw.circle(gameDisplay,white,(300,300),40)
    pygame.draw.circle(gameDisplay,red,(120,400),50)

def polygon():
    #pygame.draw.polymgon(gameDisplay,color,((x1,y1),(x2,y2),(x3,y3)))
    pygame.draw.polygon(gameDisplay, white, ((25,75),(76,125),(250,375),(400,25),(60,540)))
def line():
    #pygame.draw.line(gameDisplay,color,(x1,y1),(x2,y2),width)
    pygame.draw.line(gameDisplay,green,(100,150),(350,150),6)
    pygame.draw.line(gameDisplay,green,(100,150),(100,450),6)

def pixel():
    pixAr = pygame.PixelArray(gameDisplay)
    pixAr[100][200] = black
    pixAr[102][200] = red

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    polygon()
    rect()
    line()
    circle()
    pixel()
    
    
    pygame.display.update() 