"""this module encodes and decodes a message in an image"""
from PIL import Image

def encode(message:str, image_adress:str, key=10):
    img = Image.open(image_adress)
    w, h = img.size
    counter = 0
    message += "$END"
    for row in range(0, h, key):
        for col in range(0, w, key):
            if True:
                pass
            else:
                pass

