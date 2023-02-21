import pygame

pygame.init()

song_list = [
    "starboy.mp3", "partymonster.mp3", 
    "falsealarm.mp3", "reminder.mp3", "rockin'.mp3", 
    "secrets.mp3", "truecolors.mp3", "stargirl interlude.mp3", 
    "sidewalks.mp3", "sixfeetunder.mp3", "lovetolay.mp3", 
    "lonelynight.mp3", "attention.mp3", "ordinarylife.mp3", 
    "nothingwithoutyou.mp3", "alliknow.mp3", "dieforyou.mp3", 
    "ifeelitcoming.mp3"
    ]

song_names = [
    "Starboy", "Party Monster", "False Alarm", 
    "Reminder", "Rockin'", "Secrets", "True Colors", 
    "Stargirl Interlude", "Sidewalks", "Six Feet Under", 
    "Love To Lay", "A Lonely Night", "Attention", 
    "Ordinary Life", "Nothing Without You", 
    "All I Know", "Die For You", "I Feel It Coming"
    ]

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Starboy album player')

font = pygame.font.SysFont('sf', 24)
clock = pygame.time.Clock()
running = True

index = 0
pygame.mixer.music.load(song_list[index])
pygame.mixer.music.play()
song_name = song_names[index]
text = font.render("Currently playing:  " + song_name, True, ('black'))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        index -= 1
        pygame.mixer.music.load(song_list[index])
        song_name = song_names[index]
        text = font.render("Currently playing:  " + song_name, True, ('black'))
        pygame.mixer.music.play()
    if pressed[pygame.K_SPACE]: pygame.mixer.music.stop()
    if pressed[pygame.K_UP]: pygame.mixer.music.pause()
    if pressed[pygame.K_DOWN]: pygame.mixer.music.unpause()
    if pressed[pygame.K_RIGHT]: 
        index += 1
        pygame.mixer.music.load(song_list[index])
        song_name = song_names[index]
        text = font.render("Currently playing:  " + song_name, True, ('black'))
        pygame.mixer.music.play()
    if index == len(song_list) - 1:
        index = -1


    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load('backstar.jpg'), (0, 0))
    screen.blit(text, (22, 440))
    pygame.display.flip()
    clock.tick(5.75)
