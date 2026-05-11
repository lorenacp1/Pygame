import pygame
from entities.hamster import Hamster

pygame.init()

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hamster Heist")

clock = pygame.time.Clock()
hamster = Hamster(200, 100)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((240, 240, 240))

    ground = pygame.Rect(0, 600, WIDTH, 100)

    pygame.draw.rect(screen, (100, 200, 100), ground)
    
    
    hamster.update()
    hamster.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()