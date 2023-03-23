import pygame
from datetime import datetime
import math

pygame.init()
screen = pygame.display.set_mode((840, 840))
H_WIDTH = 840 // 2
H_HEIGHT = 840 // 2

running = True
clock = pygame.time.Clock()

pygame.display.set_caption('Mickey Mouse clock')

right_hand = pygame.image.load('right-hand.png')
left_hand = pygame.image.load('left-hand.png')

time = datetime.now()
minute = time.minute
second = time.second

angle1 = 0
angle2 = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    time = datetime.now()
    minute = time.minute
    second = time.second

    angle1 = (second*6)
    hand1 = pygame.transform.rotate(left_hand, -angle1+80)
    rect1 = hand1.get_rect()
    rect1.center = (H_WIDTH, H_HEIGHT)

    angle2 = minute*6
    hand2 = pygame.transform.rotate(right_hand, -angle2+87)
    rect2 = hand2.get_rect()
    rect2.center = (H_WIDTH, H_HEIGHT)

    screen.blit(pygame.image.load('mickeyclock.png'), (0, 0))
    screen.blit(hand1, rect1)
    screen.blit(hand2, rect2)

    pygame.display.flip()
    clock.tick(60)
