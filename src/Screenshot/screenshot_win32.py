import win32gui
import win32ui
import win32con
import win32api
import numpy as np
from PIL import Image
import time
from get_dpi_scale import *

# def get_dpi_scale_factor():
#     horizontal_pixels = win32api.GetSystemMetrics(0)  # SM_CXSCREEN
#     horizontal_virtual_pixels = win32api.GetSystemMetrics(78)  # SM_CXVIRTUALSCREEN
#
#     return horizontal_virtual_pixels / horizontal_pixels if horizontal_pixels != 0 else 1.0

def capture_window(hwnd):
    # 获取窗口位置
    dpi_scale_factor = get_scaling()
    rect = win32gui.GetWindowRect(hwnd)
    left, top, right, bottom = [int(coord * dpi_scale_factor) for coord in rect]
    # left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top

    # 创建设备上下文
    hwnd_dc = win32gui.GetWindowDC(hwnd)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()

    # 创建位图对象
    save_bitmap = win32ui.CreateBitmap()
    save_bitmap.CreateCompatibleBitmap(mfc_dc, width, height)
    save_dc.SelectObject(save_bitmap)

    # 使用BitBlt函数拷贝窗口图像到位图对象
    result = win32gui.BitBlt(save_dc.GetSafeHdc(), 0, 0, width, height, hwnd_dc, 0, 0, win32con.SRCCOPY)

    # 将位图转换为PIL图像
    bmpinfo = save_bitmap.GetInfo()
    bmpstr = save_bitmap.GetBitmapBits(True)
    img = Image.frombuffer("RGB", (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, "raw", "BGRX", 0, 1)

    # 释放资源
    win32gui.DeleteObject(save_bitmap.GetHandle())
    save_dc.DeleteDC()
    mfc_dc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwnd_dc)

    return img

begin = time.time()
# 替换为你想查找的程序的标题
window_title = "MuMu模拟器12"
hwnd = win32gui.FindWindow(None, window_title)

if hwnd != 0:
    # 截图并保存
    img = capture_window(hwnd)
    img.save("screenshot_win32.jpg")

    end = time.time()
    print(f"成功截图，保存为 screenshot_win32.jpg,用时：{int((end - begin)*1000)}ms")
else:
    print(f"未找到标题为'{window_title}'的窗口")
