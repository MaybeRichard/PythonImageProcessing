from PIL import Image

def CropImage(path,box):
    image = Image.open(path)
    crop_region = image.crop(box)
    return crop_region

def RotateImage(Pil_im,box):
    rotate_img = Pil_im.transpose(Image.ROTATE_270)
    rotate_img.paste(Pil_im,box)
    rotate_img.save("./Image/Rotated.png")

if __name__=="__main__":
    path = "./Image/Lenna.png"
    RotateImage(CropImage(path,(100,100,400,400)),(100,100,400,400))