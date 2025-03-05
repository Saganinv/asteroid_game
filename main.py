# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # clock object
    clock = pygame.time.Clock()

    # groups
    updateable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (updateable, drawables, asteroids)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawables)

    # instantiate a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    dt = 0

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()

        screen.fill((0, 0, 0))

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # limit FPS to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()