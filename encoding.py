"""this module encodes and decodes a message in an image"""

import re
import os
from PIL import Image


def encode(message: str, image_adress: str, key=10) -> str:
    """encode the message on image"""
    key %= 100
    try:
        img = Image.open(image_adress)
    except (FileNotFoundError, PermissionError):
        return f"There isn't any '{image_adress}'"
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
                if r > 255:
                    return f"'{char}' is Forbbiden"
                img.putpixel((col, row), (r, g, b))
            else:
                break
        else:
            continue
        break
    save_adress = re.sub(r"\..+$", "_encoded.png", image_adress)
    idx = 0
    while os.path.isfile(save_adress):
        idx += 1
        save_adress = re.sub(r"\(?\d*\)?\..+$", f"({idx}).png", save_adress)
    img.save(save_adress)
    img.close()
    return f"The opperation was successful.\n Image saved as '{save_adress}'"


def decode(image_adress: str, key=10) -> str:
    """decode message on image"""
    key %= 100
    message = str()
    try:
        img = Image.open(image_adress)
    except (FileNotFoundError, PermissionError):
        return f"The '{image_adress}' doesn't exist".center(30, "&")
    w, h = img.size
    for row in range(0, h, key):
        for col in range(0, w, key):
            if message[-4:] != "$END":
                r, _, _ = img.getpixel((col, row))
                message += chr(r)
            else:
                img.close()
                message = message.replace("$END", "")
                return message
    return None


if __name__ == "__main__":
    print(encode("I am not the best", "sample.jpg"))
    print(decode("sample_encoded.png"))
