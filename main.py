# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroid = pygame.sprite.Group()

Player.containers = (updateable, drawable)
Asteroid.containers = (asteroid, updateable, drawable)
AsteroidField.containers = (updateable)

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock=pygame.time.Clock()
   dt=0
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
   asteroidfield = AsteroidField()
   while True:
      screen.fill((0,0,0))
      for draw in drawable:
        draw.draw(screen)
      pygame.display.flip()
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return
      dt2=clock.tick(60)
      updateable.update(dt)
      dt=dt2/1000

if __name__ == "__main__":
    main()
