import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: float):
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.display):
        pygame.draw.circle(
            surface = screen,
            color = "white",
            center = self.position,
            radius = self.radius,
            width = LINE_WIDTH
        )


    def update(self, dt: int):
        self.position += self.velocity * dt
