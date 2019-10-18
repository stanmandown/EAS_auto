from PIL import ImageGrab
import os
#bbox=(0,1080,1980,1080)
# 第一个参数 开始截图的x坐标
# 第二个参数 开始截图的y坐标
# 第三个参数 结束截图的x坐标
# 第四个参数 结束截图的y坐标
def printScreen(num):
    pic_dir = 'pic'
    if not os.path.exists(pic_dir):
        os.mkdir(pic_dir)
    im=ImageGrab.grab(bbox=None)

    #保存
    im.save("D:/myproject/EAS_auto/EASauto/pic/"+num+".png")