import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.velocity = velocity if velocity else pygame.Vector2(0, 0)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt