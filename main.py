import pygame
from entities.hamster import Hamster

pygame.init()

WIDTH = 1200
HEIGHT = 700

menu_img = pygame.image.load("menu.png")
menu_img = pygame.transform.smoothscale(menu_img, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hamster Heist")

clock = pygame.time.Clock()

GROUND_Y = 600
INTRO_SPAWN = (WIDTH // 2, -30)
SLING_POS = (180, 520)

def create_boxes():
    return [
        pygame.Rect(880, 460, 40, 40),
        pygame.Rect(930, 460, 40, 40),
        pygame.Rect(980, 460, 40, 40), 
        pygame.Rect(905, 420, 40, 40),
        pygame.Rect(955, 420, 40, 40),
    ]

hamster = Hamster(*INTRO_SPAWN)
boxes= create_boxes()
gondola = pygame.Rect(830, 400, 290, 180)
play_button = pygame.Rect(420, 405, 360, 85)

scene = "menu"
running = True

while running:
    for event in pygame.event.get():
        if scene == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    scene = "intro"

        if event.type == pygame.QUIT:
            running = False
        
        if scene == "game":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hamster.ready and hamster.rect.collidepoint(event.pos):
                    hamster.dragging = True
    
            if event.type == pygame.MOUSEBUTTONUP:
                if hamster.dragging:
                    hamster.dragging = False
                    hamster.launched = True
                    hamster.ready = False

                    anchor_x, anchor_y = SLING_POS
                    pull_x = anchor_x - hamster.rect.centerx
                    pull_y = anchor_y - hamster.rect.centery

                    power = 0.42
                    hamster.vel_x = pull_x * power
                    hamster.vel_y = pull_y * power

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    hamster.reset_to_intro(*INTRO_SPAWN)
                    boxes = create_boxes()
                    scene = "intro"
    if scene == "menu":
        screen.blit(menu_img, (0, 0))

        #borda do botão apenas para enxergar aonde clicar
        pygame.draw.rect(screen, (255, 0, 0), play_button, 3)

    elif scene == "intro":
        screen.fill((220, 230, 245))
        pygame.draw.rect(screen, (120, 120, 120), (0, GROUND_Y, WIDTH, 100))
        intro_done = hamster.update_intro(GROUND_Y)
        if intro_done:
            scene = "game"
            hamster.prepare_for_game(*SLING_POS)

        hamster.draw(screen)

    elif scene == "game":
        if hamster.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            anchor_x, anchor_y = SLING_POS
            max_pull = 140

            dx = max(-max_pull, min(max_pull, mouse_x - anchor_x))
            dy = max(-max_pull, min(max_pull, mouse_y - anchor_y))

            hamster.rect.center = (anchor_x + dx, anchor_y + dy)

        hamster.update_game(GROUND_Y)

        for box in boxes[:]:
            if hamster.rect.colliderect(box):
                boxes.remove(box)

        screen.fill((240, 240, 240))
        pygame.draw.rect(screen, (100, 200, 100), (0, GROUND_Y, WIDTH, 100))
        pygame.draw.rect(screen, (120, 120, 120), gondola)

        for box in boxes:
            pygame.draw.rect(screen, (200, 150, 50), box)
        
        if hamster.dragging: 
            pygame.draw.line(screen, (0, 0, 0), SLING_POS, hamster.rect.center,)

        hamster.draw(screen)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()