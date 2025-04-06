import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Always destroy the current asteroid
        self.kill()

        # If this is a small asteroid, we're done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calculate new properties for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_angle = random.uniform(20, 50)

        # Create two new velocity vectors
        vel1 = self.velocity.rotate(split_angle) * 1.2
        vel2 = self.velocity.rotate(-split_angle) * 1.2

        # Create two new smaller asteroids
        ast1 = Asteroid(self.position.x, self.position.y, new_radius) # type: ignore
        ast2 = Asteroid(self.position.x, self.position.y, new_radius) # type: ignore

        # Set their velocities
        ast1.velocity = vel1
        ast2.velocity = vel2

