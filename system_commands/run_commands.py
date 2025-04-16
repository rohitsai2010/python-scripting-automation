import subprocess


command = ["dir"] if subprocess.os.name == "nt" else ["ls", "-l"]

try:
    subprocess.run(command, check=True, shell=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
