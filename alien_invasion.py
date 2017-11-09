#--coding:utf-8--

import pygame
from pygame.sprite import Group

from settings import setting
from ship import Ship
import game_function as gf

def run_game():
    #初始化pygame、设置屏幕对象
    pygame.init()
    ai_setting = setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_setting,screen)
    #创建一个存储子弹的编组
    bullets = Group()


    #开始游戏主循环
    while True:
        gf.check_events(ai_setting,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_setting,ship,screen,bullets)

run_game()
