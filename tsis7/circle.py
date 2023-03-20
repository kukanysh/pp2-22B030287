import pygame
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((640, 480))
x = 28
y = 28

color = ((255, 0, 0 ))

running = True

clock = pygame.time.Clock()
pygame.display.set_caption('drawing circle')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=20
    if pressed[pygame.K_DOWN]: y+=20
    if pressed[pygame.K_LEFT]: x-=20
    if pressed[pygame.K_RIGHT]: x+=20

    if x <= 28:
        x = 28
    elif x >= 612:
        x = 612
    if y <= 28:
        y = 28
    elif y >= 452:
        y = 452
    

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), 25)

    pygame.display.flip()
    clock.tick(25)