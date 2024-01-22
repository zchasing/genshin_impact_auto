import os.path

import win32gui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImage
import sys
import time

from src.path import PATH_DATA_IMGRES


def get_screenshot():
    # 创建QApplication实例和初始化
    app = QApplication(sys.argv)

    begin = time.time()
    hwnd = win32gui.FindWindow(None, "MuMu模拟器12")

    # 获取主屏幕
    screen = QApplication.primaryScreen()

    # 获取窗口截图
    img = screen.grabWindow(hwnd).toImage()

    # end = time.time()
    # 保存截图
    # img.save("screenshot_pyqt.jpg")

    # print(f"成功截图，保存为 screenshot_pyqt.jpg，用时：{int((end - begin) * 1000)}ms")

    return img

if __name__ == "__main__":
    img = get_screenshot()
    img.save(os.path.join(PATH_DATA_IMGRES, "screenshot_pyqt.jpg"))
