#--coding:utf-8--

import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_setting,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:  # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  #空格键，开火
        fire_bullet(ai_setting,screen,ship,bullets)


def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_setting,screen,ship,bullets):
    #响应鼠标和按键事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #关闭窗口则退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_setting,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_setting,ship,screen,bullets):
    #更新屏幕上图案，并切换到新屏幕
    # 每次循环之后都重绘屏幕
    screen.fill(ai_setting.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""

    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_setting,screen,ship,bullets):
    """如果还没到限制，就发射一颗子弹"""
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)