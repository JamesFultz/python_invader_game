import sys
import pygame
from settings import Settings

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Invasion")
    
    # Background Color
    bg_color = (230, 230, 230)
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        # Redraw the screen durig each pass through the loop.
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Make the moust recently drawn screen visible.
        pygame.display.flip()
        
run_game()