import pygame
from constants import *
from circleshape import CircleShape
from player import Player


def main():
    pygame.init()
    
    screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Asteroids")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    """
    So there are three parts to the game loop:
    1: Handle events
        what is a event handler?
    2: update game world/state
        we do this with a for loop to cycle through all the objects in the game 
    3: draw the game to the screen
        once the for loop is done we then draw the game onto the screen and the for loop starts again
    ___________
    Setting up FPS next, or delta time, how ever you want to call it. ill limit the game to 60 fps.
    
    """
    #game loop starting
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return running == False
                
        for obj in updatable:
            obj.update(dt)
                
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    
    
