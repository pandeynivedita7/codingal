# Import Necessary Libraries
import pygame

# Initialize required modules
#Basic Pygame Window
pygame.init()

# Setup window geometry
screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Basic Pygame Window")

# Create a loop to run till the game is quit by the user
done = False

while not done:
    # Clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # stop the loop

    # Fill screen with white color
    screen.fill((255, 255, 255))#RGB

    # Make the changes visible
    pygame.display.flip()

# Quit pygame
pygame.quit()