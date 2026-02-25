# import logging
# import os
# from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# logs_dir = os.path.join(os.getcwd(), "logs")
# os.makedirs(logs_dir, exist_ok=True)   # ✅ create logs directory only

# LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# if __name__ == "__main__":
#     logging.info("Logging started")


import logging
import os
from datetime import datetime

# Project root (safer than os.getcwd())
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logger = logging.getLogger("firstmlproject")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    formatter = logging.Formatter(
        "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

# Optional console logging
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)