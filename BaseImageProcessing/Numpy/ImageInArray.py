from PIL import Image
from pylab import *

'''
    读取图像并以不同的颜色、浮点数类型来编码
'''

im = array(Image.open("./Image/Lenna.png"))
print(im.shape,im.dtype)

im = array(Image.open("./Image/Lenna.png").convert('L'),'f')
print(im.shape,im.dtype)