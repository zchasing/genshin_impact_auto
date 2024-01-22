import matplotlib.pyplot as plt
from PyQt5.QtGui import QImage
import numpy as np
import cv2


def qimg2cv2(qimage):
    # 获取图像的字节数组
    byte_array = qimage.convertToFormat(4)

    # 获取图像的尺寸
    width, height = qimage.width(), qimage.height()

    # 将字节数组转换为 NumPy 数组
    ptr = byte_array.bits()
    ptr.setsize(qimage.byteCount())
    img_array = np.array(ptr).reshape(height, width, 4)

    # 如果图像是 RGB 格式而不是 BGR，进行通道交换
    img_array_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGBA2BGR)

    # plt.Figure()
    # plt.imshow(img_array_bgr)
    # plt.show(block=True)

    return img_array_bgr
