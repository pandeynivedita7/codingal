import pygame

# Initialize Pygame
pygame.init()

# Create the display surface object of specific dimension
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Draw Circles")

# Define colors
GREEN = (0, 255, 0)#RGB
RED=(255,0,0)
WHITE = (255, 255, 255)

# Fill the screen with white color
window.fill(WHITE)

# Draw solid circle (x=300, y=300, radius=50)
pygame.draw.circle(window, GREEN, (300, 300), 50)

# Draw outlined circle (x=100, y=100, radius=50, thickness=3)
pygame.draw.circle(window, GREEN, (100, 100), 50, 3)

# Update display to show shapes
pygame.display.update()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
