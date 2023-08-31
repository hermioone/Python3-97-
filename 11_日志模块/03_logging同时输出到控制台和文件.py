# 既要把日志输出到终端，也输出到文件

import logging
import traceback


# 1. 创建一个 logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)          # Log 默认等价

# 2. 创建一个 handler，用于写入日志文件
file_handler = logging.FileHandler(
    filename="./log.txt", mode="a", encoding="UTF-8")
file_handler.setLevel(logging.WARNING)

# 3. 再创建一个 handler，用于输出到控制台
console_handler = logging.StreamHandler()
# 取 handler 的 log 级别和 logger 的 log 级别中高的那个级别
console_handler.setLevel(logging.DEBUG)

# 4. 定义 handler 的输出格式
formatter = logging.Formatter(
    "%(asctime)s - %(filename)s[line:%(lineno)d]) - %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 5. 将 logger 添加到 handler 中
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 日志
logger.debug("这是 debug")
logger.info("这是 info")
logger.warning("这是 warning")
logger.error("这是 error")
logger.critical("这是 critical")

try:
    b = 1/0
except Exception as e:
    # 打印异常堆栈
    err_msg = traceback.format_exc()
    logger.error(
        f"exception occurs: {e}, \n{err_msg}")
