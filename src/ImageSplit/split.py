import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

from src.ImageIdentification.qimg2cv2 import qimg2cv2
from src.Screenshot.screenshot_pyqt import get_screenshot_pyqt
from src.path import PATH_DATA_IMGRES

split_part = {"part1": [0, 0, 400, 800], "part2": [300, 400, 500, 1000]}


def img_spilt(img_arr):
    img_parts = []
    for key, value in split_part.items():
        imgpart = img_arr[value[0]:value[2], value[1]:value[3]]
        img_parts.append(imgpart)
    return img_parts


if __name__ == "__main__":
    # img = get_screenshot_pyqt()
    # screenshot = qimg2cv2(img)
    screenshot = cv2.imread(os.path.join(PATH_DATA_IMGRES, "screenshot_pyqt.jpg"))
    screenshot_rgb = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
    img_parts = img_spilt(screenshot_rgb)
    num = len(img_parts)

    plt.Figure()
    for index, imgs in enumerate(img_parts):
        plt.subplot(1, num, index + 1)
        plt.imshow(imgs)
    plt.show(block=True)
