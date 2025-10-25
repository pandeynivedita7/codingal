import pygame
import random
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing - Avoid Obstacles")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)

# Clock & Font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# ---- 🎵 Load Sounds ----
try:
    pygame.mixer.music.load(r"racing-racing-speed-action-music-290637.mp3")  # background music
    crash_sound = pygame.mixer.Sound(r"car-crash-382137.mp3")     # crash sound
    pygame.mixer.music.play(-1)  # loop background music forever
except:
    print("⚠️ Could not load sound files, continuing without sound")
    crash_sound = None

# Load player car
try:
    car_img = pygame.image.load(r"car.png")
    car_img = pygame.transform.scale(car_img, (60, 100))
except:
    print("⚠️ Could not load car.png, using rectangle instead")
    car_img = None

car_x = WIDTH // 2 - 30
car_y = HEIGHT - 120
car_speed = 7

# Obstacles
obstacles = []
obstacle_speed = 7
spawn_delay = 1500  # ms
pygame.time.set_timer(pygame.USEREVENT + 1, spawn_delay)

score = 0
game_over = False

# Main loop
running = True
while running:
    clock.tick(60)
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Spawn obstacles
        if event.type == pygame.USEREVENT + 1 and not game_over:
            obs_x = random.randint(100, WIDTH - 160)
            obstacles.append({"x": obs_x, "y": -120, "w": 60, "h": 100})

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_x -= car_speed
        if keys[pygame.K_RIGHT]:
            car_x += car_speed

        # Keep car inside road
        car_x = max(100, min(car_x, WIDTH - 160))

        # Move obstacles
        for obs in obstacles:
            obs["y"] += obstacle_speed

        # Remove passed obstacles
        obstacles = [obs for obs in obstacles if obs["y"] < HEIGHT]

        # Check collisions
        for obs in obstacles:
            if (car_x < obs["x"] + obs["w"] and car_x + 60 > obs["x"] and
                car_y < obs["y"] + obs["h"] and car_y + 100 > obs["y"]):
                game_over = True
                if crash_sound:
                    crash_sound.play()  # 💥 play crash sound once

        # Draw road boundaries
        pygame.draw.rect(screen, YELLOW, (90, 0, 10, HEIGHT))
        pygame.draw.rect(screen, YELLOW, (WIDTH - 100, 0, 10, HEIGHT))

        # Draw player car
        if car_img:
            screen.blit(car_img, (car_x, car_y))
        else:
            pygame.draw.rect(screen, WHITE, (car_x, car_y, 60, 100))

        # Draw obstacles
        for obs in obstacles:
            pygame.draw.rect(screen, RED, (obs["x"], obs["y"], obs["w"], obs["h"]))

        # Update score
        score += 1
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    else:
        # Game Over Screen
        over_text = font.render("GAME OVER", True, RED)
        screen.blit(over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
        score_text = font.render(f"Final Score: {score}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - 120, HEIGHT // 2 + 20))

    pygame.display.flip()

pygame.quit()
sys.exit()
