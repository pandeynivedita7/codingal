import pygame

# Initialize Pygame
pygame.init()

# Colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
RED = (200, 0, 0)

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Screen Elements")

# Font setup
font = pygame.font.SysFont("Times New Roman", 32)

# Main loop
running = True
while running:
    # Fill background
    screen.fill(WHITE)

    # Draw a circle
    pygame.draw.circle(screen, GREEN, (200, 300), 50)

    # Draw a rectangle (x, y, width, height)
    pygame.draw.rect(screen, BLUE, (400, 250, 150, 100))

    # Draw text
    text_surface = font.render("Nivedita Pygame Program", True, RED)
    screen.blit(text_surface, (250, 100))

    # Update display
    pygame.display.flip()

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()