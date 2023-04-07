import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Collision detection 1 using colliderect")

car = pygame.image.load('images//racecar.png')
# co- ordinaed of car
car_box = car.get_rect()
obstacle = pygame.Rect(200,400,80,80)

vel = 10

def quit_game():
        global run
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

def movement():
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT]:
        car_box.x -= vel
    if userInput[pygame.K_RIGHT]:
        car_box.x += vel
    if userInput[pygame.K_UP]:
        car_box.y -= vel
    if userInput[pygame.K_DOWN]:
        car_box.y += vel

def collision():
      if car_box.colliderect(obstacle):
            pygame.draw.rect(screen,(255,0,0),(car_box.x-10,car_box.y-10,car_box.w+20,car_box.h+20),4)
            
run = True
while run:
        quit_game()
        screen.fill((255,255,255))

        movement()

        screen.blit(car,car_box)
        pygame.draw.rect(screen,(0,0,0),obstacle,4)

        collision()

        pygame.time.delay(30)
        pygame.display.update()
