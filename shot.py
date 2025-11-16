import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: int, y: int, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.display):
            pygame.draw.circle(
                surface = screen,
                color = "red",
                center = self.position,
                radius = self.radius,
                width = 0
            )

    def update(self, dt: int):
        self.position += self.velocity * dt