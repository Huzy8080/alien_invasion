import sys
import pygame


def check_events():
    """响应鼠标和按键的事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_setting, screen, ship):
    """更新屏幕上的图像，并刷新画面"""
    # 填充背景颜色
    screen.fill(ai_setting.bg_color)
    # 绘制飞船
    ship.blitme()
    # 重绘屏幕
    pygame.display.flip()
