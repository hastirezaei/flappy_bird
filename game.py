import pygame
import sys

pygame.init()

main_screen = pygame.display.set_mode((456, 645))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(80)
    
    