# Asteroids
from constants import *
from player import Player
import pygame

player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, PLAYER_RADIUS=PLAYER_RADIUS)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
