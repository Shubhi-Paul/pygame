import pygame, sys

def bouncing_rect():

    global x_speed, y_speed , other_speed

    moving_rect.x += x_speed
    moving_rect.y += y_speed

    other_rect.y += other_speed
    if other_rect.top <= 0 or other_rect.bottom >= screenHeight:
        other_speed *= -1

    # collision with screen borders
    if (moving_rect.right >= screenWidth or moving_rect.left <= 0):
        x_speed *= -1
    if (moving_rect.bottom >= screenHeight or moving_rect.top <= 0):
        y_speed *= -1

    # collision with rect
    collision_tolerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1
        if abs(other_rect.left - moving_rect.right) < collision_tolerance and x_speed > 0:
            x_speed *= -1


    pygame.draw.rect(screen, (255,255,255), moving_rect)
    pygame.draw.rect(screen,(255,0,0),other_rect)

pygame.init()
clock = pygame.time.Clock()
screenWidth,screenHeight = 850,550
screen = pygame.display.set_mode((screenWidth,screenHeight))

moving_rect = pygame.Rect(400,100,50,50)
x_speed,y_speed = 6,5

other_rect = pygame.Rect(375,250,100,50)
other_speed = 3

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30,30,30))
    bouncing_rect()
    pygame.display.flip()
    clock.tick(60)