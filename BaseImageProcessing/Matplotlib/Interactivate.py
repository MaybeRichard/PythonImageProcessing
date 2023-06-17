from PIL import Image
from pylab import *

'''
    交互式标注：用户点击n个点，记录点击的n个点的坐标
'''
im = array(Image.open("./Image/Lenna.png"))

imshow(im)

print("Please click 3 points")
x = ginput(3)
print("You Click:",x)
show()