import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Draw Rectangle")

# Game loop flag
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill background with white
    screen.fill((255, 255, 255))#RGB
    
    # Draw a rectangle (x=30, y=30, width=60, height=60)
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
