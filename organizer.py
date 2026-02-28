import os
import shutil

SOURCE_FOLDER = "test_folder"

FILE_TYPES = {
    "Images": [".jpg", ".png"],
    "Documents": [".pdf", ".docx"],
    "Videos": [".mp4"]
}

def organize_files():
    for filename in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, filename)

        if os.path.isfile(file_path):
            for folder, extensions in FILE_TYPES.items():
                if filename.endswith(tuple(extensions)):
                    folder_path = os.path.join(SOURCE_FOLDER, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, filename))
                    print(f"Moved {filename} to {folder}")

if __name__ == "__main__":
    organize_files()