import logging
import os
import sys

# __all__ = ['logger']

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'output.log'))
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
sh = logging.StreamHandler()  # 往屏幕上输出
logger.addHandler(sh)
logger.addHandler(handler)

if __name__ == '__main__':
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
