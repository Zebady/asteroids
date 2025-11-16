import pygame
from random import uniform
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: float):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        rnd_angle = uniform(20, 50)

        # New smaller asteroid (one)
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, rnd_angle) * 1.2

        # New smaller asteroid (two)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -rnd_angle) * 1.2

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
