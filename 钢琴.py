import pygame
 # 初始化Pygame
pygame.init()
 # 设置钢琴键的音符
notes = {
    pygame.K_z: 'C4',
    pygame.K_s: 'D4',
    pygame.K_x: 'E4',
    pygame.K_c: 'F4',
    pygame.K_v: 'G4',
    pygame.K_b: 'A4',
    pygame.K_n: 'B4',
    pygame.K_m: 'C5',
}
 # 主循环
def main_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         # 获取当前按下的键
        keys = pygame.key.get_pressed()
         # 检查每个键是否按下
        for key, note in notes.items():
            if keys[key]:
                play_note(note)
 # 播放音符
def play_note(note):
    pygame.mixer.music.load(r'C:\Users\86176\Desktop\Amazon/{note}.wav')  # 替换为音符音频文件的路径
    pygame.mixer.music.play()
 # 运行钢琴模拟器
def run_piano_simulator():
    main_loop()
run_piano_simulator()