import os
import time

folder_path = "./logs"
days_old = 7
now = time.time()

if os.path.exists(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path,file)
        if file.endswith(".log"):
            file_age = now-os.path.getmtime(file_path)
            if file_age > days_old * 86400:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
else:
    print("Log folder Does not Exist.")                
