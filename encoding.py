"""this module encodes and decodes a message in an image"""
from PIL import Image

def encode(message:str, image_adress:str, key=10):
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
                pass

    img.save("sample.png")

if __name__ == "__main__":
    encode("amin", "sample.jpg")
    img = Image.open("sample.png")
    print(chr(img.getpixel((40,0))[0]))
