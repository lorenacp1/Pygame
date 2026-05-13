import pygame
from entities.hamster import Hamster

pygame.init()

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hamster Heist")

clock = pygame.time.Clock()
hamster = Hamster(200, 100)

ground_y = 600

gondola = pygame.Rect(850, 520, 200, 80)

boxes = [
    pygame.Rect(880, 480, 40, 40), 
    pygame.Rect(930, 480, 40, 40),
    pygame.Rect(905, 440, 40, 40),
]

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

                mouse_x, mouse_y = event.pos

                hamster.vel_x = (hamster.rect.centerx - mouse_x)*0.2
                hamster.vel_y = (hamster.rect.centery - mouse_y)*0.2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                hamster.reset()

    if hamster.dragging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        sling_x, sling_y = hamster.start_pos
        max_pull = 100

        dx = mouse_x - sling_x
        dy = mouse_y - sling_y 

        dx = max_(-max_pull, min(max_pull, dx))
        dy = max(-max_pull, min(max_pull, dy))

        hamster.rect.center = (sling_x + dx, sling_y + dy)

    hamster.update()

    for box in boxes[:]:
        if hamster.rect.colliderect(box):
            boxes.remove(box)

    screen.fill((240, 240, 240))

    pygame.draw.rect(screen, (100, 200, 100), (0, ground_y, WIDTH, 100))

    pygame.draw.rect(screen, (120, 120, 120), gondola)

    for box in boxes:
        pygame.draw.rect(screen, (200, 150, 50), box)
    
    hamster.draw(screen)
    
    pygame.display.update()
    clock.tick(60)


pygame.quit()