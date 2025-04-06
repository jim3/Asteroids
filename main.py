import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Set the containers for classes
    Player.containers = (updatable, drawable) # type: ignore
    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore
    AsteroidField.containers = (updatable,) # type: ignore
    Shot.containers = (shots, updatable, drawable) # type: ignore
    
    # Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                return

            # Check for bullet-asteroid collisions
            # Check for bullet-asteroid collisions
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()  # Changed from asteroid.kill()
                    shot.kill()            
            # for shot in shots:
            #     if shot.collides_with(asteroid):
            #         asteroid.kill()
            #         shot.kill()

        # Draw everything
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()