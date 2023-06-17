from PIL import Image

'''创建图像缩略图'''

'''
    Create ThumbNail
    
    Args:
        path: path of a image
        size: size of thumbnail
    
'''
def create_thumbnail(path,size):
    image = Image.open(path)
    image.thumbnail((size))
    image.save("./Image/thumb.png")
    

if __name__ =="__main__":
    create_thumbnail(r"C:\Users\Richard\Documents\Code\PythonImageProcessing\Image\Lenna.png",(128,128))
