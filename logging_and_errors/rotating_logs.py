import logging
from logging.handlers import RotatingFileHandler

# Set up rotating logging
logger = logging.getLogger("RotatingLog")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler("rotating_app.log", maxBytes=500, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

for i in range(100):
    logger.info(f"Log entry {i}")
