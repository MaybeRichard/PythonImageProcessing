from PIL import Image

'''
    旋转和调整图像尺寸
'''
'''
    Resize image.

    Args:
        path: path of image
        size: size to be resized
    
    Return:
        resized image(PIL.Image.Image)
'''
def Resize(path,size):
    return Image.open(path).resize((size))

'''
    Rotate image.

    Args:
        path: path of image
        size: angle to be rotated
    
    Return:
        rotated image(PIL.Image.Image)
'''
def Rotate(path,angle):
    img = Image.open(path)
    img = img.rotate(angle)
    # img.save("./Image/rotated.png")
    return img

if __name__ =="__main__":
    path = "./Image/Lenna.png"
    resized_img = Resize(path=path,size=(256,256))
    resized_img.save("./Image/resized.png")
    img = Rotate(path=path,angle=45)
    print(type(img))
    img.save("./Image/rotated.png")