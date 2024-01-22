import win32gui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QLineEdit, QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap

class ScreenshotApp(QMainWindow):
    # 初始化窗口
    def __init__(self):
        super().__init__()
        self.initUI()
        self.signal_connection()
        self.timer_setup()
        

    # 自定义ui窗口
    def initUI(self):
        # 新建窗口
        central_widget = QWidget(self)
        # 将当前窗口置为中心窗口，焦点在这个窗口,初始化尺寸
        self.setCentralWidget(central_widget)
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle('Screenshot Example')
        
        # 新建布局控制器
        layout = QVBoxLayout(central_widget)
        # 新建标签，用于显示图像
        self.label = QLabel(self)
        # 将标签添加到布局中
        layout.addWidget(self.label)
        # Checkbox
        self.cb_auto_screen = QCheckBox('自动截图', self)
        layout.addWidget(self.cb_auto_screen)
        self.cb_auto_screen.setChecked(True)
        self.lb_time_interval = QLabel('截图间隔，单位ms:', self)
        layout.addWidget(self.lb_time_interval)
        self.le_time_interval = QLineEdit()
        layout.addWidget(self.le_time_interval)
        self.le_time_interval.setText('50')
        # 按钮
        self.screenshot_button = QPushButton('Take Screenshot', self)
        layout.addWidget(self.screenshot_button)
        # 设置定时器
        self.timer = QTimer(self)
        self.msg_flag = 0
    
    def signal_connection(self):
        self.screenshot_button.clicked.connect(self.take_screenshot)
        self.timer.timeout.connect(self.take_screenshot)
        self.le_time_interval.editingFinished.connect(self.timer_setup)
        self.cb_auto_screen.stateChanged.connect(self.timer_setup)
    
    def timer_setup(self):
        # 设置定时器时间，每隔一段时间更新截图.
        if self.cb_auto_screen.isChecked():
            self.le_time_interval.setEnabled(True)
            time_interval = self.get_time_interval()
            if time_interval:
                self.timer.start(time_interval)  # 单位ms
            # else:
            #     self.le_time_interval.setText('10')
        else:
            self.timer.stop()
            self.le_time_interval.setEnabled(False)
    
    def get_time_interval(self):
        try:
            value = self.le_time_interval.text()
            value = int(value)
            return value
        except:
            QMessageBox.information(None, '提示', '请输入整数！')
    def take_screenshot(self):
        # 寻找窗口
        hwnd = win32gui.FindWindow(None, "MuMu模拟器12")
        # 获取主屏幕
        screen = QApplication.primaryScreen()
        # 获取窗口截图
        img = screen.grabWindow(hwnd).toImage()
        # 存在窗口则显示，否则输出未找到
        if img:
            # 将img转换为pixmap用于在标签中显示
            pixmap = QPixmap.fromImage(img)
            # 计算宽高，等下等比缩放
            w_o = pixmap.width()
            h_o = pixmap.height()
            w = 800
            h = int(w / w_o * h_o)
            # 等比缩放
            pixmap = pixmap.scaled(w, h, aspectRatioMode=1)

            # 将截图显示在 QLabel 中
            self.label.setPixmap(pixmap)
        else:
            print("Window not found.")

# 格式程序，不用管
if __name__ == '__main__':
    app = QApplication([])
    window = ScreenshotApp()
    window.show()
    app.exec_()

