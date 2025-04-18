# Logging and Error Handling in Python

This module contains examples of logging and handling errors using Python’s built-in `logging` module.

## Scripts

### 1. `basic_logging.py`
- Logs messages at all levels (DEBUG to CRITICAL).
- Outputs to a file called `app.log`.

### 2. `rotating_logs.py`
- Demonstrates rotating logs when a file exceeds a certain size.
- Keeps up to 3 backup log files.

### 3. `try_except_logging.py`
- Logs an exception caught in a try-except block.
- Stores error details in `error.log`.

## Requirements
No external libraries — all are built into Python.

## How to Run
```bash
python basic_logging.py
python rotating_logs.py
python try_except_logging.py
