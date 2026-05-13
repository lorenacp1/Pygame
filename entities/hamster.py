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

    def update(self):
        if self.dragging:
            return
        
        if self.launched:
            self.vel_y += self.gravity
            self.rect.y += int(self.vel_y)
            self.rect.x += int(self.vel_x)

            if self.rect.bottom >= 600:
                self.rect.bottom = 600
                self.vel_y = self.vel_y * -0.4
                self.vel_x = self.vel_x * 0.8

                if abs(self.vel_y) < 1:
                    self.vel_y = 0
                if abs(self.vel_x) < 0.5:
                    self.vel_x = 0
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)
