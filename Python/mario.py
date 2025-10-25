import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 215, 0)
BROWN = (139, 69, 19)

# Game variables
GRAVITY = 0.8
JUMP_STRENGTH = -15
PLAYER_SPEED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.vel_x = 0
        self.on_ground = False
        self.score = 0
        self.lives = 3

    def update(self, platforms):
        keys = pygame.key.get_pressed()

        # Horizontal movement
        self.vel_x = 0
        if keys[pygame.K_LEFT]:
            self.vel_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.vel_x = PLAYER_SPEED

        # Apply gravity
        self.vel_y += GRAVITY

        # Jump
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False

        # Update position
        self.rect.x += self.vel_x
        self.check_collision_x(platforms)

        self.rect.y += self.vel_y
        self.on_ground = False
        self.check_collision_y(platforms)

        # Keep player on screen horizontally
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        # Fall off screen (death)
        if self.rect.top > HEIGHT:
            self.lives -= 1
            self.rect.x = 100
            self.rect.y = 200
            self.vel_y = 0

    def check_collision_x(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0:
                    self.rect.right = platform.rect.left
                elif self.vel_x < 0:
                    self.rect.left = platform.rect.right

    def check_collision_y(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, move_range):
        super().__init__()
        self.image = pygame.Surface((35, 35))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.move_range = move_range
        self.direction = 1
        self.speed = 2

    def update(self):
        self.rect.x += self.speed * self.direction

        if self.rect.x > self.start_x + self.move_range or self.rect.x < self.start_x:
            self.direction *= -1

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mario Platformer")
    clock = pygame.time.Clock()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # Create player
    player = Player(100, 200)
    all_sprites.add(player)

    # Create platforms
    platform_data = [
        (0, HEIGHT - 40, WIDTH, 40),  # Ground
        (200, 450, 150, 20),
        (400, 350, 150, 20),
        (600, 250, 150, 20),
        (100, 150, 150, 20),
        (500, 500, 100, 20),
    ]

    for x, y, w, h in platform_data:
        p = Platform(x, y, w, h)
        platforms.add(p)
        all_sprites.add(p)

    # Create coins
    coin_positions = [
        (250, 400), (450, 300), (650, 200),
        (150, 100), (550, 450), (300, 500)
    ]

    for x, y in coin_positions:
        c = Coin(x, y)
        coins.add(c)
        all_sprites.add(c)

    # Create enemies
    enemy_data = [
        (250, 425, 80),
        (450, 325, 80),
    ]

    for x, y, r in enemy_data:
        e = Enemy(x, y, r)
        enemies.add(e)
        all_sprites.add(e)

    # Game loop
    running = True
    font = pygame.font.Font(None, 36)

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        player.update(platforms)
        enemies.update()

        # Check coin collection
        collected_coins = pygame.sprite.spritecollide(player, coins, True)
        player.score += len(collected_coins)

        # Check enemy collision
        if pygame.sprite.spritecollide(player, enemies, False):
            player.lives -= 1
            player.rect.x = 100
            player.rect.y = 200
            player.vel_y = 0

        # Check game over
        if player.lives <= 0:
            running = False

        # Draw
        screen.fill(BLUE)
        all_sprites.draw(screen)

        # Draw UI
        score_text = font.render(f"Score: {player.score}", True, WHITE)
        lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        pygame.display.flip()

    # Game over screen
    screen.fill(BLACK)
    game_over_text = font.render("GAME OVER", True, RED)
    final_score_text = font.render(f"Final Score: {player.score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    screen.blit(final_score_text, (WIDTH // 2 - 120, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()