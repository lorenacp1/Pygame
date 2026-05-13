import pygame

class Hamster:
    def __init__(self, x, y):
        
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (180, 120, 80), (25, 25), 25)

        self.rect = self.image.get_rect(topleft=(x, y))

        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 0.5

        self.dragging = False
        self.launched = False
        self.ready = False
        self.intro_falling = True 
    
    def reset_to_intro(self, x, y):
        self.rect.center = (x,y)
        self.vel_x = 0
        self.vel_y = 0
        self.dragging = False
        self.launched = False
        self.ready = False
        self.intro_falling = True

    def prepare_for_game(self, x, y): 
        self.rect.center = (x,y)
        self.vel_x = 0
        self.vel_y = 0
        self.dragging = False
        self.launched = False
        self.ready = True
        self.intro_falling = False

    def update_intro(self, ground_y):
        self.vel_y += self.gravity
        self.rect.y += int(self.vel_y)

        if self.rect.bottom >= ground_y:
            self.rect.bottom = ground_y
            self.vel_y = 0
            self.intro_falling = False
            return True

        return False

    def update_game(self, ground_y): 
        if self.dragging:
            return 
        
        if self.launched: 
            self.vel_y += self.gravity 
            self.rect.x += int(self.vel_x)
            self.rect.y += int(self.vel_y)

            if self.rect.bottom >= ground_y:
                self.rect.bottom = ground_y
                self.vel_x = 0
                self.vel_y = 0
                self.launched = False
                self.ready = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
