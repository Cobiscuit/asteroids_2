import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scoreboard import Scoreboard


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score_group = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Scoreboard.containers = (score_group, drawable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    
    scoreboard = Scoreboard(screen, "Score: 0", SCREEN_WIDTH // 2, 30, 36, (255, 255, 255))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                player.lose_life()
                if player.lives == 0:
                    print("Game over!")
                    sys.exit()
                else:
                    # Reset player's position to the center or where they died
                    player.reset_position(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score += 10
                    print(score)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        scoreboard.draw_text(screen, f"Score: {score} Lives: {player.lives}", SCREEN_WIDTH // 2, 30, 36, (255, 255, 255))
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()