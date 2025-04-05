import os

os.makedirs("new_folders", exist_ok=True)

os.rename("new_folders", "renamed_folder")

os.rmdir("renamed_folder")