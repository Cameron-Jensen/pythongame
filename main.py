# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroid = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updateable, drawable)
Asteroid.containers = (asteroid, updateable, drawable)
AsteroidField.containers = (updateable)
Shot.containers = (shots, updateable, drawable)

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock=pygame.time.Clock()
   dt=0
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
   asteroidfield = AsteroidField()
   timer = 0
   while True:
      screen.fill((0,0,0))
      for draw in drawable:
        draw.draw(screen)
      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
      for sprite in asteroid:
        if sprite.collision(player) == True:
          print("Game over!")
          exit() 
      # Add in your main loop, after checking player-asteroid collisions
      for shot in shots.copy():  # Use .copy() to avoid modification during iteration
        for asteroid_obj in asteroid.copy():  # Same here
          if shot.collision(asteroid_obj):
            shot.kill()  # Remove shot from all groups
            asteroid_obj.split()  # Remove asteroid from all groups
            timer = PLAYER_SHOOT_COOLDOWN
            break  # Break after handling one collision per shot
      dt2=clock.tick(60)
      updateable.update(dt)
      dt=dt2/1000
      timer -= dt

if __name__ == "__main__":
    main()
