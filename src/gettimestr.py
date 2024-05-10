import time


def gettimestr():
    # 获取当前时间戳
    current_timestamp = time.time()

    # 将时间戳转换为 struct_time 对象
    current_time = time.localtime(current_timestamp)

    # 格式化日期时间字符串作为文件名
    formatted_datetime = time.strftime("%Y-%m-%d_%H-%M-%S", current_time)

    # 生成文件名
    custom_filename = f"screenshot_{formatted_datetime}.jpg"

    return custom_filename
