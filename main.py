import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
print("Screen width:", SCREEN_WIDTH)
print("Screen height:", SCREEN_HEIGHT)

def main():
  pygame.init()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()

  dt = 0.0

  while True:
    log_state()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    screen.fill("black")

    dt = clock.tick(60) / 1000

    pygame.display.flip()

main()