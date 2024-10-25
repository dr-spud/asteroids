import pygame
from constants import *
from player import *
from asteroid import *
from  asteroidfield import *
from circleshape import CircleShape
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()


    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill(0)
        

        for entity in updatable:
            entity.update(dt)
        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over!")
                sys.exit()

        for entity in drawable:
            entity.draw(screen)


        pygame.display.flip()


        # limit fps to 60
        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()
