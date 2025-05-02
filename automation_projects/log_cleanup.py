import os
import time
import logging

log_folder = "logs"
days_old = 3
now = time.time()

logging.basicConfig(filename="cleanup.log", level=logging.INFO,
                    format='%(asctime)s - %(message)s')

if os.path.exists(log_folder):
    for file in os.listdir(log_folder):
        file_path = os.path.join(log_folder, file)
        if file.endswith(".log"):
            file_age = now - os.path.getmtime(file_path)
            if file_age > days_old * 86400:
                os.remove(file_path)
                logging.info(f"Deleted: {file_path}")
else:
    logging.warning(f"{log_folder} does not exist.")
