import pygame
from constants import *

def main():
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    """
    So there are three parts to the game loop:
    1: Handle events
        what is a event handler?
    2: update game world/state
        we do this with a for loop to cycle through all the objects in the game 
    3: draw the game to the screen
        once the for loop is done we then draw the game onto the screen and the for loop starts again
    """
    #game loop starting
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
                
        
    
    
    
    
    
    
    
    
    
    




if __name__ == "__main__":
    main()
    
    
