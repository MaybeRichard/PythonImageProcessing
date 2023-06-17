from PIL import Image
from pylab import *

'''
    对图像进行灰度变换
'''

im = array(Image.open("./Image/Lenna.png").convert('L'))

im2 = 255-im #对图像进行反相处理

im3 = (100.0/255)*im + 100

im4 = 255.0*(im/255.0)**2

figure()

subplot(4,1,1)
imshow(im)
title('Original')

subplot(4,1,2)
imshow(im2)
title('Original')

subplot(4,1,3)
imshow(im3)
title('Original')

subplot(4,1,4)
imshow(im4)
title('Original')

show() 

print(int(im.max()),int(im.min()))