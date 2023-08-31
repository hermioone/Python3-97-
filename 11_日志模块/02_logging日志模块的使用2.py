import logging
import traceback


logging.basicConfig(level=logging.WARNING,
                    filename="./log.txt",
                    filemode="a",           # a 是追加
                    encoding="UTF-8",
                    format="%(asctime)s - %(filename)s[line:%(lineno)d]) - %(levelname)s: %(message)s")


logging.debug("这是 debug")
logging.info("这是 info")
logging.warning("这是 warning")
logging.error("这是 error")
logging.critical("这是 critical")

try:
    b = 1/0
except Exception as e:
    # 打印异常堆栈
    err_msg = traceback.format_exc()
    logging.error(
        f"exception occurs: {e}, \n{err_msg}")
