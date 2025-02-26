# Asteroids
import sys
from constants import *
from player import (Player, Shot)
from asteroid import Asteroid
import pygame
from asteroidfield import AsteroidField



def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, PLAYER_RADIUS=PLAYER_RADIUS)

    while True:
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print ("Game Over") 
                sys.exit()
        for shot in shots:
            for asteroid in asteroids:
                if shot.collision(asteroid):
                    new_asteroids = asteroid.split()  # Call `split()` instead of `kill()`
                    if new_asteroids:  # If splitting creates new asteroids
                        for new_asteroid in new_asteroids:
                            asteroids.add(new_asteroid)  # Add to 'asteroids' group
                            updatable.add(new_asteroid)  # Add to 'updatable' group
                            drawable.add(new_asteroid)   # Add to 'drawable' group
                    asteroid.kill()  # Remove the original asteroid
                    shot.kill()  # Also remove the shot
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
