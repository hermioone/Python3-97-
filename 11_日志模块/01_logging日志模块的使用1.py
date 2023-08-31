import logging

logging.basicConfig(level=logging.WARNING,
                    format="%(asctime)s - %(filename)s[line:%(lineno)d]) - %(levelname)s: %(message)s")


logging.debug("这是 debug")
logging.info("这是 info")
logging.warning("这是 warning")
logging.error("这是 error")
logging.critical("这是 critical")
