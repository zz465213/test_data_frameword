import logging
import os
from configs.common_paths import LOG_DIR

# 定義日誌訊息的格式
LOG_LEVEL = logging.INFO
LOG_DATE_FORMAT = "%Y%m%d_%H%M%S"
LOG_FILENAME = os.path.join(LOG_DIR, "log")
LOG_FORMAT = "%(asctime)s - %(filename)s:%(lineno)d - %(name)s - %(levelname)s - %(message)s"
LOG_FILE_FORMAT = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT)
