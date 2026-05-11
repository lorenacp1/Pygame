import pygame

class Hamster:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.radius = 20

        self.vel_x = 0
        self.vel_y = 0

        self.gravity = 0.5

        self.dragging = False

    def update(self):

        self.vel_y += self.gravity

        self.y += self.vel_y
        self.x += self.vel_x

        ground_y = 600

        if self.y + self.radius > ground_y:

            self.y = ground_y - self.radius

            self.vel_y = 0

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (160, 120, 80),
            (int(self.x), int(self.y)),
            self.radius
        )
