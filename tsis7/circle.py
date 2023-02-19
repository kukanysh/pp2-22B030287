import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
running = True
x = 30
y = 30
surface = pygame.Surface((50, 50))
color = ((255, 0, 0 ))
pygame.draw.circle(surface, color, (x, y), 25)
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
    
    screen.fill((255, 255, 255))
    

    pygame.display.flip()
    clock.tick(60)