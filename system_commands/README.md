# System Command Automation with Subprocess

This module uses Python's `subprocess` module to run and manage system-level commands.

## Scripts

### 1. `run_commands.py`
- Runs basic system commands like `dir` (Windows) or `ls` (Linux/macOS).
- Uses `subprocess.run()` with error handling.

### 2. `subprocess_output_handler.py`
- Executes a command and captures its output and errors.
- Demonstrates using `capture_output=True` and `text=True`.

## Requirements
No external libraries — just the built-in `subprocess` module.

## How to Run
```bash
python run_commands.py
python subprocess_output_handler.py
