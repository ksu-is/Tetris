import pygame

pygame.init()

winSize = (600,400)


displayScreen = pygame.display.set_mode(winSize)

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            sys.exit()
    pygame.display.update()

