import sys

from loguru import logger
from src.path import *
import os


def check_and_create_file(path, file_name):
    # 获取文件路径
    file_path = os.path.join(path, file_name)

    # 检查目录是否存在，如果不存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"目录 '{path}' 不存在，已创建。")

    # 检查文件是否存在
    if not os.path.exists(file_path):
        # 如果文件不存在，可以在这里添加创建文件的代码
        with open(file_path, 'w') as file:
            file.write("")

        print(f"文件 '{file_path}' 不存在，已创建。")
    else:
        print(f"文件 '{file_path}' 已存在。")


check_and_create_file(PATH_DATA_SETTING, "General.json")

logger.add(os.path.join(PATH_DATA_SETTING, 'Logs', "{time:YYYY-MM-DD}/{time:YYYY-MM-DD}.log"), level="TRACE", backtrace=True)

logger.success("A success message.")
logger.error("An error message.")
logger.critical("A critical message.")
