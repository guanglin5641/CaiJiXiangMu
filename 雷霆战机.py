import pygame
import random
 # 初始化Pygame
pygame.init()
 # 定义屏幕尺寸
screen_width = 800
screen_height = 600
 # 创建屏幕对象
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("飞行射击游戏")
 # 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
 # 加载图像
player_img = pygame.image.load(r"C:\Users\86176\Desktop\Amazon\image/a.jpg")
enemy_img = pygame.image.load(r"C:\Users\86176\Desktop\Amazon\image/b.jpg")
 # 定义玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed_x = 0
    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
 # 定义敌人类

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randint(1, 3)
    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed_y = random.randint(1, 3)
 # 创建玩家和敌人精灵组
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
 # 游戏主循环
running = True
clock = pygame.time.Clock()
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0
     # 更新游戏状态
    all_sprites.update()
     # 碰撞检测
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False
     # 绘制屏幕
    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()
     # 控制帧率
    clock.tick(60)
 # 退出游戏
pygame.quit()