# import pygame
# import time
# def main():
#     screen=pygame.display.set_mode((1196,790),0,32)   #窗口大小
#     background=pygame.image.load(r"C:\Users\Administrator\Desktop\aa.png")  #图片位置
#     while True:   #循环刷新
#         screen.blit(background,(0,0))  #对齐的坐标
#         pygame.display.update()   #显示内容
#         time.sleep(0.01)   #延迟时间
# if __name__=="__main__":
#     main()

class Settings():
    """存储外星人所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船设置

        self.ship_limit = 3
        # 子弹设置

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 外星人设置
        # 外星人移动
        self.fleet_drop_speed = 10

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化动态设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移动，为-1向左移动
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # 外星人点数
        self.alien_points = int(self.alien_points * self.score_scale)



