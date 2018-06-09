import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()   # 初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))   # 创建一个宽1200像素，高800像素的游戏窗口
    pygame.display.set_caption("Alien Invasion")

    # 创建“开始”按钮
    play_button = Button(ai_settings, screen, "开始")

    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #创建一艘飞船、一个用于存储子弹的编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)   # 监视键盘和鼠标事件

        if stats.game_active:
            ship.update()   # 更新飞船的位置
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)  # 更新所有未消失子弹的位置
            # 在更新子弹后再更新外星人的位置，因为稍后要检查是否有子弹撞到了外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)    # 绘制屏幕


run_game()