from PIL import Image
import os

'''
    转换图片格式,如果图片格式不是jpg，则转换为jpg格式，如果是jpg格式，则不转换
'''

def convert_image_format(path):
    image = Image.open(path)
    # 利用splitext()函数获取文件名和后缀名，利用后缀名判断图片格式是否为jpg
    prefix,suffix = os.path.splitext(path)

    if suffix != '.jpg':
        image.save(prefix+'.jpg')
        print('图片格式转换成功！')
    else:
        print('图片格式为jpg，不需要转换！')


if __name__ == '__main__':
    path = input('请输入图片路径：')
    convert_image_format(path)
    
