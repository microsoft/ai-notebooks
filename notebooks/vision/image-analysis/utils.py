import requests
from matplotlib import pyplot as plt
from PIL import Image
from io import BytesIO
import numpy as np
import cv2 as cv


def url2pil(input_img):
    try:
        response = requests.get(input_img)
        return Image.open(BytesIO(response.content))
    except:
        print(response, input_img)

def np2pil(input_img, flag_bgr2rgb=True):
    if flag_bgr2rgb:
        input_img = bgr2rgb(input_img)
    return Image.fromarray(input_img)

def bgr2rgb(input_img):
    return cv.cvtColor(input_img, cv.COLOR_BGR2RGB)

def imshow(input_img, crop=(), flag_bgr2rgb=True):
    plt.figure()
    if isinstance(input_img, str):
        img = url2pil(input_img)
    elif isinstance(input_img, np.ndarray):
        img = np2pil(input_img, flag_bgr2rgb)
    else:
        img = input_img
    try:
        if len(crop) == 4:
            img = img.crop((crop[0], crop[1], crop[0]+crop[2], crop[1]+crop[3]))
        plt.axis("off")
        plt.imshow(img)
        return img
    except:
        pass
