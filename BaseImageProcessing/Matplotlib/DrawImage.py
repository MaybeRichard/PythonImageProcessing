from PIL import Image
import pylab

'''
    使用matplotlib绘制点和线，pylab是matplotlib的一个模块
'''
# 读取图像到数组中
im = pylab.array(Image.open("./Image/Lenna.png"))

pylab.imshow(im)

# 设置点坐标
x = [100,100,400,400]
y = [200,500,200,500]

# 绘制几个点为红色星号
pylab.plot(x,y,'r*')
# 绘制一条直线，从（100，100）到（200，500）
pylab.plot([100,100],[200,500])
pylab.title('Plotting: "empire.jpg"')
pylab.show()