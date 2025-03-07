# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   clock=pygame.time.Clock()
   dt=0
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
   while True:
      screen.fill((0,0,0))
      player.draw(screen)
      pygame.display.flip()
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              return
      dt2=clock.tick(60)
      player.update(dt)
      dt=dt2/1000

if __name__ == "__main__":
    main()
