import os
import pygame

chinese_dir = 'chinese'
if not os.path.exists(chinese_dir):
    os.mkdir(chinese_dir)
#pygame初始化
pygame.init()
def tagetCOM():
    text = u"GZAYSYJYQZC"
#设置字体和字号
    font = pygame.font.SysFont('Microsoft YaHei', 12)
#字体大小非常影响精度
#渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
    ftext = font.render(text, True, (0, 0, 0),(255, 255, 255))
#保存图片
    pygame.image.save(ftext, "D:\myproject\EAS_auto\EASauto\chinese\open.png")#图片保存地址
tagetCOM()

