import subprocess

try:
    result = subprocess.run(["python", "--version"], capture_output=True, text=True, check=True)
    print("Command output:")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"An error occurred:\n{e.stderr}")
