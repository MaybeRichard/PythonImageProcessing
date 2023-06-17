from PIL import Image
import pylab
import matplotlib.pyplot as plt 
import numpy 
'''
    使用matplotlib绘制点和线，pylab是matplotlib的一个模块
'''
# 读取图像到数组中
im = numpy.array(Image.open("./Image/Lenna.png"))

plt.imshow(im)

# 设置点坐标
x = [100,100,400,400]
y = [200,500,200,500]

# 绘制几个点为红色星号
plt.plot(x,y,'r*')
# 绘制一条直线，从（100，100）到（200，500）
plt.plot([100,100],[200,500])
plt.title('Plotting: "empire.jpg"')
plt.show()