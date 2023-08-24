import os

def get_folder_size(folder_path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)

    size_bytes = total_size

    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    size_gb = size_mb / 1024


    print(f"Total size: {size_bytes} bytes, {size_kb:.2f} KB, {size_mb:.2f} MB, {size_gb:.2f} GB")

    return total_size


get_folder_size(R"C:\Users\MAKE\Downloads")
