#--coding:utf-8

import pygame

class Ship(object):
    """初始化飞船并设置初始位置"""

    def __init__(self,ai_setting,screen):
        self.screen = screen
        self.ai_setting = ai_setting
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()    #self.image???====前一项的image啊，获取image的矩形
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """根据移动标志调整飞船位置"""
        #跟新飞船center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left: #原点（0,0）位于屏幕左上角,所以可改写为self.rect.left > 0
            self.center -= self.ai_setting.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.center
