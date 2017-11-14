#--coding:utf-8--

import pygame
from pygame.sprite import Group

from settings import setting
from ship import Ship
import game_function as gf
from alien import Alien

def run_game():
    #初始化pygame、设置屏幕对象
    pygame.init()
    ai_setting = setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船,创建一个存储子弹的编组和一个外星人编组
    ship = Ship(ai_setting,screen)
    bullets = Group()
    aliens = Group()

    #创建一个外星人群
    gf.create_fleet(ai_setting,screen,aliens)

    #开始游戏主循环
    while True:
        gf.check_events(ai_setting,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_setting,aliens)
        gf.update_screen(ai_setting,screen,ship,aliens,bullets)

run_game()
