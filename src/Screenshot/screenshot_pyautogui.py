import pygetwindow as gw
import pyautogui
import time

begin = time.time()

# 替换为你想查找的程序的标题
window_title = "MuMu模拟器12"

# 获取窗口位置
window = gw.getWindowsWithTitle(window_title)

if window:
    window = window[0]

    # 获取窗口位置
    x, y, width, height = window.left, window.top, window.width, window.height

    # 使用pyautogui截图
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # 保存截图
    screenshot.save("screenshot_pyautogui.png")

    end = time.time()
    print(f"成功截图，保存为 screenshot_pyautogui.png,用时：{int((end - begin)*1000)}ms")
else:
    print(f"未找到标题为'{window_title}'的窗口")

