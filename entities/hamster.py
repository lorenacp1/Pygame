import pygame

class Hamster:
    def __init__(self, x, y):
        
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (180, 120, 80), (25, 25), 25)

        self.rect = self.image.get_rect(topleft=(x, y))

        self.rest_pos = (x, 600 - self.rect.height)

        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 0.5

        self.dragging = False
        self.launched = False
        self.intro_falling = True 
        self.ready = False

    def update(self):
        if self.dragging:
            return
        
        if self.intro_falling:
            self.vel_y += self.gravity
            self.rect.y += int(self.vel_y)

            if self.rect.bottom >= 600:
                self.rect.bottom = 600
                self.vel_y = 0
                self.iintro_falling = False
                self.ready = True

            return
        
        if self.launched:
            self.vel_y += self.gravity
            self.rect.y += int(self.vel_y)
            self.rect.x += int(self.vel_x)

            if self.rect.bottom >= 600:
                self.rect.bottom = 600
                self.vel_y = 0
                self.vel_x = 0
                self.launched = Falseself.ready = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self): 
        self.rect.topleft = self.start_pos
        self.vel_x = 0
        self.vel_y = 0
        self.dragging = False
        self.launched = False
