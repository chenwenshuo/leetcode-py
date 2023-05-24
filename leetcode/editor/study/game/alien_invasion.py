import sys

import pygame

from leetcode.editor.study.game.setting_alien import Settings


def run_game():
    pygame.init()
    setting = Settings()
    sc = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("alien_invasion")

    while True:
        for event in pygame.event.get():
            sc.fill(setting.bg_color)
            if event.type == pygame.QUIT:
                sys.exit()

            pygame.display.flip()

run_game()