import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from logger import log_event

print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
print("Screen width:", SCREEN_WIDTH)
print("Screen height:", SCREEN_HEIGHT)

def main():
  pygame.init()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()

  dt = 0.0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  Player.containers = (updatable, drawable)

  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2

  player = Player(x, y)
  # Create groups
  asteroids = pygame.sprite.Group()

  # Set container groups
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)

  # Instantiate asteroid field before the game loop starts
  asteroid_field = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill("black")

    dt = clock.tick(60) / 1000

    updatable.update(dt)

    for render in drawable:
      render.draw(screen)

    pygame.display.flip()

    for asteroid in asteroids:
        if asteroid.collides_with(player):
            log_event("player_hit")
            print("Game over!")
            sys.exit()

    log_state()

main()
