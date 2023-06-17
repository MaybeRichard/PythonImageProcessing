from PIL import Image
from pylab import *

'''
    绘制图像的轮廓和直方图
'''

im = array(Image.open("./Image/Lenna.png").convert('L')) # 这里的array实际上是Numpy.array，因为pylab中包含了一些numpy的内容
figure()
gray()

# 使用 `pylab.contour()` 函数绘制图像的轮廓图。
# `origin='image'` 参数表示轮廓的起点应与图像的原点对齐。
contour(im,origin='image')
# 设置坐标轴的比例为相等，并关闭坐标轴。
axis('equal')
axis('off')

figure()
hist(im.flatten(),128)
show()