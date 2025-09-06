"""this module encodes and decodes a message in an image"""
from PIL import Image
import re

def encode(message:str, image_adress:str, key=10):
    key %= 100
    img = Image.open(image_adress)
    w, h = img.size
    counter = 0
    message += "$END"
    for row in range(0, h, key):
        for col in range(0, w, key):
            counter += 1
            if counter <= len(message):
                r, g, b = img.getpixel((col, row))
                char = message[counter - 1]
                r = ord(char)
                img.putpixel((col, row), (r, g, b))
            else:
                break
        else:
            continue
        break
    save_adress = re.sub(r"\..+$", "_encoded.png", image_adress)
    img.save(save_adress)

def decode(image_adress:str, key=10):
    key %= 100
    message = str()
    img = Image.open(image_adress)
    w, h = img.size
    for row in range(0, h, key):
        for col in range(0, w, key):
            if True:
                r, g, b = img.getpixel((col, row))
                print(chr(r), end=" |")
            else:
                pass
if __name__ == "__main__":
    decode("sample.png")
