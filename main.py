import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  # gets all modules of pygame
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  # pygame containers
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  
  Player.containers = (updatable, drawable)
  Shot.containers = (shots, updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  asteroid_field = AsteroidField()

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  # game loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    updatable.update(dt)

    for asteroid in asteroids:
      if asteroid.check_collision(player):
        sys.exit("Game over!")

      for bullet in shots:
        if bullet.check_collision(asteroid):
          asteroid.split()
          bullet.kill()

    screen.fill("black")
    for obj in drawable:
      obj.draw(screen)
    
    # updates full display to screen
    pygame.display.flip()
    # limits framerate to 60FPS
    dt = clock.tick(60) / 1000
    


if __name__ == "__main__":
  main()