import os
import shutil

path = input("Enter the path: ")

try:
    if not os.path.exists(path):
        print("Path doesn't exist")

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if not os.path.isfile(file_path):
            continue
        name, ext = os.path.splitext(file)
        ext = ext.lower()

        if ext in (".jpg", ".jpeg", ".png"):
            folder_name = "Images"
        elif ext in (".mp4", ".wmv", ".avi", ".mpg", ".mpeg"):
            folder_name = "Videos"
        elif ext in (".mp3", ".wav"):
            folder_name = "Music"
        elif ext in (".txt", ".pdf", ".doc", ".docx"):
            folder_name = "Documents"
        else:
            folder_name = "Others"

        new_folder_path = os.path.join(path, folder_name)
        os.makedirs(new_folder_path, exist_ok=True)

        shutil.move(file_path, os.path.join(new_folder_path, file))

except Exception as e:
    print("Unexpected error:", e)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    print("Files have been successfully organized!")



