import os
import shutil

os.makedirs("new_folders", exist_ok=True)
with open("new_folders/sample.txt", "w") as f:
    f.write("this is the first file for the automation")

os.makedirs("second_folder", exist_ok=True)

shutil.copy("new_folders/sample.txt", "second_folder/copied.txt")

shutil.move("new_folders/sample.txt", "second_folder/moved.txt")