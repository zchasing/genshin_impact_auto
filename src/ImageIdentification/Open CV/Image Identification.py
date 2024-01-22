import os
from matplotlib import pyplot as plt
from src.Screenshot.screenshot_pyqt import get_screenshot
from src.ImageIdentification.qimg2cv2 import qimg2cv2
from src.path import PATH_DATA_IMGRES
import cv2
import numpy as np

def match_template(image, template_path, threshold=0.8):
    # 读取输入图像和模板图像
    template = cv2.imread(template_path)

    # 转换为灰度图像
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 使用归一化相关性系数匹配方法
    method = cv2.TM_CCOEFF_NORMED

    # 执行模板匹配
    result = cv2.matchTemplate(image_gray, template_gray, method)

    # 找到匹配结果中的最大值和最大值的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 判断是否匹配成功
    if max_val > threshold:
        print("模板匹配成功！")
        # 在原始图像中绘制矩形框
        w, h = template_gray.shape[::-1]
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

        # 显示结果
        plt.Figure()
        plt.imshow(image)
        plt.show(block=True)
    else:
        print("模板匹配失败！")

if __name__ == "__main__":
    # 输入图像和模板图像路径
    img = get_screenshot()
    screenshot = qimg2cv2(img)
    template_path = os.path.join(PATH_DATA_IMGRES, "imgres0.jpg")

    # 设置匹配阈值（可调整）
    matching_threshold = 0.9

    # 执行匹配
    match_template(screenshot, template_path, matching_threshold)



