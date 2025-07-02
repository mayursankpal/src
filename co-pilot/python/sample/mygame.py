#write a basic skeleton of a game using pygame
import pygame
import sys
from pygame.locals import *
# Initialize Pygame
pygame.init()
# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('My Game')
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
        
        # Fill the screen with white
        screen.fill(WHITE)
        
        # Draw a black rectangle
        pygame.draw.rect(screen, BLACK, (WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2))
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)
    
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()