import pygame.font


class ScoreBoard():
    """显示得分信息的类"""

    def __init__(self, screen, ai_settings, stats):
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats
        self.screen_rect = screen.get_rect()

        # 显示得分信息的字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """将得分转换为一幅图像"""
        round_socre = int(round(self.stats.score, -1))
        score_str = "{:,}".format(round_socre)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
