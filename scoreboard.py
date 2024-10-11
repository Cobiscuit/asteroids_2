import pygame
class Scoreboard:
    def __init__(self, screen, text, x, y, size, color):
      pass  
        
    def draw_text(self, screen, text, x, y, size, color):
        font = pygame.font.Font(None, size)
        text = font.render(text, True, color)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
        