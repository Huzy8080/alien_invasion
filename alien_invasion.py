import pygame
from pygame.sprite import Group

import game_functions as gf
from button import Button
from game_stats import GameStats
from scoreboard import ScoreBoard
from settings import Settings
from ship import Ship


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 开始按钮
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    # 记分牌
    score_board = ScoreBoard(screen, ai_settings, stats)
    # 创建一艘飞船
    ship = Ship(screen, ai_settings)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # 开始游戏主循环
    while True:
        # 监听事件
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens, score_board)
        if stats.game_active:
            # 更新飞船位置
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, aliens, ship, bullets, stats, score_board)
            # 更新外星人
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 更新画面
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, score_board)


run_game()
