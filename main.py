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
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hamster.rect.collidepoint(event.pos):
                hamster.dragging = True
    
        if event.type == pygame.MOUSEBUTTONUP:
            if hamster.dragging:
                hamster.dragging = False
                hamster.launched = True

                mouse_x, mouse_y = pygame.mouse.get_pos()

                hamster.vel_x = (hamster.rect.centerx - mouse_x)*0.2
                hamster.vel_y = (hamster.rect.centery - mouse_y)*0.2

    if hamster.dragging:
        hamster.rect.center = pygame.mouse.get_pos()
    

    keys = pygame.key.get_pressed()
    

    screen.fill((240, 240, 240))

    ground = pygame.Rect(0, 600, WIDTH, 100)

    pygame.draw.rect(screen, (100, 200, 100), ground)
    
    hamster.update()
    hamster.draw(screen)
    pygame.display.update()
    clock.tick(60)


pygame.quit()