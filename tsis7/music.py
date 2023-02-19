import pygame
import os

_sound_library = {}
def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()

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

screen = pygame.display.set_mode((400, 600))
running = True
pygame.mixer.music.load('starboy.mp3')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: pygame.mixer.music.play()
    if pressed[pygame.K_RIGHT]: pygame.mixer.music.stop()
    if pressed[pygame.K_UP]: pygame.mixer.music.pause()
    if pressed[pygame.K_DOWN]: pygame.mixer.music.unpause()
    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load('black.jpg'), (0, 0))
    screen.blit(get_image('starboy.jpeg'), (100, 110)) #starboy

    pygame.display.flip()
