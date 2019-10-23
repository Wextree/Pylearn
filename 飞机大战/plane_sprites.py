import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 程序每秒的帧数
FPS = 60

# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 创建子弹的定时常量
HERO_FIRE_ENVENT = pygame.USEREVENT+1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        """在屏幕的垂直方向移动"""
        self.rect.y += self.speed

class Background(GameSprite):
    """背景精灵类"""

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")

        if is_alt == True:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        super().__init__("./images/enemy1.png")

        self.speed = random.randint(1, 4)
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        super().__init__("./images/me1.png", 0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        # 控制精灵不能移出屏幕
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right >= SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width

    def fire(self):
        for i in (0, 1, 2):
            bullet = Bullet()

            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx =self.rect.centerx

            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵类"""

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()