import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, controlled=False):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.controlled = controlled  # whether player controls this sprite

        # Give random velocity if not controlled
        if not controlled:
            self.velocity = [random.choice([-3, 3]), random.choice([-3, 3])]

    def update(self, keys=None):
        if self.controlled:
            # Move using arrow keys
            if keys[pygame.K_LEFT]:
                self.rect.x -= 5
            if keys[pygame.K_RIGHT]:
                self.rect.x += 5
            if keys[pygame.K_UP]:
                self.rect.y -= 5
            if keys[pygame.K_DOWN]:
                self.rect.y += 5
        else:
            # Bounce automatically
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.velocity[0] = -self.velocity[0]
            if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
                self.velocity[1] = -self.velocity[1]

# Sprite group
all_sprites = pygame.sprite.Group()

# Create one controlled sprite (red, positioned at bottom-left)
player = Sprite(RED, 40, 40, 50, HEIGHT - 60, controlled=True)

# Create one auto-moving sprite (blue, positioned randomly)
enemy = Sprite(BLUE, 40, 40, random.randint(100, 500), random.randint(50, 300))

# Add to group
all_sprites.add(player)
all_sprites.add(enemy)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys for player movement
    keys = pygame.key.get_pressed()

    # Update sprites
    all_sprites.update(keys)

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Limit FPS
    clock.tick(60)

pygame.quit()