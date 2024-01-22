import numpy as np
from PyQt5.QtGui import QImage, QPixmap

def arr2qimg(img_array):
    if len(img_array.shape) == 2:  # 灰度图像
        height, width = img_array.shape
        img_array = np.stack((img_array,) * 3, axis=-1)  # 转换为3通道的RGB
    else:  # RGB图像
        height, width, _ = img_array.shape

    bytes_per_line = 3 * width  # 假设3通道（RGB）
    qimage = QImage(img_array.data, width, height, bytes_per_line, QImage.Format_RGB888)

    return qimage