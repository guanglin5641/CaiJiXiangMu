import pygame
import random
 # 初始化游戏
pygame.init()
 # 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 # 设置窗口大小
window_width = 800
window_height = 600
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("贪吃蛇")
 # 定义贪吃蛇的初始位置和大小
snake_block_size = 20
snake_speed = 15
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)
 # 定义计分函数
def your_score(score):
    value = score_font.render("得分：" + str(score), True, WHITE)
    window.blit(value, [10, 10])
 # 定义贪吃蛇的绘制函数
def our_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_block_size, snake_block_size])
 # 定义游戏主循环
def game_loop():
    game_over = False
    game_close = False
     # 贪吃蛇的初始位置
    x1 = window_width / 2
    y1 = window_height / 2
     # 贪吃蛇的初始移动方向
    x1_change = 0
    y1_change = 0
     # 定义贪吃蛇的身体长度
    snake_list = []
    length_of_snake = 1
     # 随机生成食物的位置
    foodx = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0
     # 游戏主循环
    while not game_over:
        while game_close == True:
            # 游戏结束时的处理
            window.fill(BLACK)
            message = font_style.render("游戏结束！按Q退出，按C重新开始", True, WHITE)
            window.blit(message, [window_width / 6, window_height / 3])
            your_score(length_of_snake - 1)
            pygame.display.update()
             # 处理游戏结束时的按键事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
         # 处理贪吃蛇的移动事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0
         # 处理贪吃蛇撞到墙壁时的游戏结束事件
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
         # 更新贪吃蛇的位置
        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)
        pygame.draw.rect(window, RED, [foodx, foody, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
         # 控制贪吃蛇的长度
        if len(snake_list) > length_of_snake:
            del snake_list[0]
         # 处理贪吃蛇吃到自己时的游戏结束事件
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
         # 绘制贪吃蛇和食物
        our_snake(snake_block_size, snake_list)
        your_score(length_of_snake - 1)
         # 更新窗口
        pygame.display.update()
         # 处理贪吃蛇吃到食物时的事件
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, window_height - snake_block_size) / 20.0) * 20.0
            length_of_snake += 1
         # 控制贪吃蛇的速度
        pygame.time.Clock().tick(snake_speed)
     # 退出游戏
    pygame.quit()
 # 开始游戏
game_loop()