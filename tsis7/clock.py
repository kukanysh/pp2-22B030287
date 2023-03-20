import pygame
import datetime

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

pygame.init()
screen = pygame.display.set_mode((800, 600))
running= True
pygame.display.set_caption('Clock app')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((27, 67, 123))
    screen.blit(pygame.image.load('mickeyclock.jpeg'), (0, 0))

    pygame.display.flip()
