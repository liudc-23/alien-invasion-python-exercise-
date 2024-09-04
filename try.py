import pygame
import sys

pygame.init()
screen = pygame.display.set_mode( (1200,800 ) )
while True:
    screen.fill((230,230,230))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_q:
                sys.exit()
    pygame.display.flip()

