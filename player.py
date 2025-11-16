import pygame
from circleshape import CircleShape
from shot import Shot
from constants import (
        PLAYER_RADIUS,  
        PLAYER_TURN_SPEED, 
        PLAYER_SPEED, 
        SHOT_RADIUS,
        PLAYER_SHOOT_SPEED,
        PLAYER_SHOOT_COOLDOWN_SECONDS
)

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0.0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.display):
        pygame.draw.polygon(
            surface = screen, 
            color = "blue", 
            points = self.triangle(), 
            width = 0
        )

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def rotate(self, dt: int):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self, dt: int):
        if self.shot_cooldown <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            unit_vector = pygame.Vector2(0, 1)
            rotated_vector = unit_vector.rotate(self.rotation)
            rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
            shot.velocity += rotated_with_speed_vector
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

    def update(self, dt: int):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

        self.shot_cooldown -= dt