# mario_game.py
import pygame
import random
import os
import sys

WIDTH, HEIGHT = 800, 480
FPS = 60
GRAVITY = 0.6
PLAYER_SPEED = 4
JUMP_POWER = -12
COIN_RESPAWN_TIME = 1500

ASSETS = {
    'background': 'background.png',
    'player': 'realmario.png',
    'coin': 'money.png',
    'enemy': 'badman.png',
    'bgmusic': 'bgmusic.mp3',
    'jump': 'jump.wav',
    'coin_sound': 'coin.wav'
}


def load_image(name, scale=None):
    if os.path.exists(name):
        img = pygame.image.load(name).convert_alpha()
        if scale:
            img = pygame.transform.smoothscale(img, scale)
        return img
    return None


def load_sound(name):
    if os.path.exists(name):
        try:
            return pygame.mixer.Sound(name)
        except:
            return None
    return None


# -------------------------------------------------------------
# PLAYER
# -------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image=None):
        super().__init__()
        if image:
            self.image = image
        else:
            self.image = pygame.Surface((40, 60))
            self.image.fill((50, 150, 250))

        self.rect = self.image.get_rect(midbottom=(x, y))
        self.vel_y = 0
        self.on_ground = False

    def update(self, keys):
        dx = 0
        if keys[pygame.K_LEFT]:
            dx = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            dx = PLAYER_SPEED

        self.rect.x += dx
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.bottom >= HEIGHT - 40:
            self.rect.bottom = HEIGHT - 40
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def jump(self, jump_sound=None):
        if self.on_ground:
            self.vel_y = JUMP_POWER
            self.on_ground = False
            if jump_sound:
                try:
                    jump_sound.play()
                except:
                    pass


# -------------------------------------------------------------
# COIN
# -------------------------------------------------------------
class Coin(pygame.sprite.Sprite):
    def __init__(self, image=None):
        super().__init__()
        if image:
            self.image = image
        else:
            self.image = pygame.Surface((24, 24), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (255, 215, 0), (12, 12), 12)

        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.center = (
            random.randint(60, WIDTH - 60),
            random.randint(60, HEIGHT - 120)
        )


# -------------------------------------------------------------
# ENEMY
# -------------------------------------------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image=None, patrol=150, speed=2):
        super().__init__()
        if image:
            self.image = image
        else:
            self.image = pygame.Surface((40, 40))
            self.image.fill((200, 30, 30))

        self.rect = self.image.get_rect(midbottom=(x, y))
        self.start_x = x
        self.patrol = patrol
        self.speed = speed
        self.dir = 1

    def update(self):
        self.rect.x += self.speed * self.dir

        if self.rect.x > self.start_x + self.patrol:
            self.dir = -1
        if self.rect.x < self.start_x - self.patrol:
            self.dir = 1


# -------------------------------------------------------------
# MAIN GAME
# -------------------------------------------------------------
def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mini Mario Game")

    clock = pygame.time.Clock()

    bg = load_image(ASSETS['background'], scale=(WIDTH, HEIGHT))
    player_img = load_image(ASSETS['player'], scale=(48, 68))
    coin_img = load_image(ASSETS['coin'], scale=(28, 28))
    enemy_img = load_image(ASSETS['enemy'], scale=(44, 44))

    jump_sound = load_sound(ASSETS['jump'])
    coin_sound = load_sound(ASSETS['coin_sound'])

    if os.path.exists(ASSETS['bgmusic']):
        try:
            pygame.mixer.music.load(ASSETS['bgmusic'])
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        except:
            pass

    player = Player(200, HEIGHT - 40, player_img)
    coin = Coin(coin_img)
    enemy = Enemy(WIDTH - 150, HEIGHT - 40, enemy_img)

    coins = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    coins.add(coin)
    enemies.add(enemy)

    all_sprites = pygame.sprite.Group(player, coin, enemy)

    score = 0
    font = pygame.font.SysFont(None, 30)
    bigfont = pygame.font.SysFont(None, 50)
    game_over = False
    last_coin_time = None

    while True:
        dt = clock.tick(FPS)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over:
                if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_UP):
                    player.jump(jump_sound)

            if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                main()

        if not game_over:
            enemy.update()
            player.update(keys)

            hit_coin = pygame.sprite.spritecollideany(player, coins)
            if hit_coin:
                score += 10
                if coin_sound:
                    try:
                        coin_sound.play()
                    except:
                        pass
                hit_coin.kill()
                last_coin_time = pygame.time.get_ticks()

            if last_coin_time and pygame.time.get_ticks() - last_coin_time >= COIN_RESPAWN_TIME:
                new_coin = Coin(coin_img)
                coins.add(new_coin)
                all_sprites.add(new_coin)
                last_coin_time = None

            if pygame.sprite.spritecollideany(player, enemies):
                game_over = True
                try:
                    pygame.mixer.music.fadeout(500)
                except:
                    pass

        if bg:
            screen.blit(bg, (0, 0))
        else:
            screen.fill((92, 148, 252))
            pygame.draw.rect(screen, (100, 200, 100), (0, HEIGHT - 40, WIDTH, 40))

        all_sprites.draw(screen)

        scr = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(scr, (10, 10))

        if game_over:
            t1 = bigfont.render("GAME OVER", True, (255, 50, 50))
            t2 = font.render("Press R to Restart", True, (255, 255, 255))
            screen.blit(t1, (WIDTH//2 - t1.get_width()//2, HEIGHT//2 - 40))
            screen.blit(t2, (WIDTH//2 - t2.get_width()//2, HEIGHT//2 + 10))

        pygame.display.flip()


if __name__ == "__main__":
    main()
