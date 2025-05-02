import shutil
import os
from datetime import datetime

source_folder = "important_files"
backup_folder = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

try:
    shutil.copytree(source_folder, backup_folder)
    print(f"Backup successful: {backup_folder}")
except FileNotFoundError:
    print("Source folder does not exist.")
except Exception as e:
    print(f"Backup failed: {e}")
