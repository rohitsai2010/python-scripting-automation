# Mini Automation Projects in Python

This module contains simple, practical Python scripts that automate everyday file system tasks.

## Scripts

### 1. `folder_backup_automation.py`
- Creates a timestamped backup of a folder using `shutil.copytree`.
- Handles missing source folders and general errors.

### 2. `log_cleanup_automation.py`
- Deletes `.log` files older than 3 days.
- Logs all deletions and warnings in `cleanup.log`.

## Requirements
Uses built-in libraries like `os`, `time`, `shutil`, `logging`, and `datetime`.

## How to Run
```bash
python folder_backup_automation.py
python log_cleanup_automation.py
