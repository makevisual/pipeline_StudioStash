import psutil #psutil is a secondary package
import os

# returns the size of a disk, returning a list with the total_space, used_space, and free_space, in bytes
def get_disk_space(path):
    disk_usage = psutil.disk_usage(path)
    total_space = disk_usage.total
    used_space = disk_usage.used
    free_space = disk_usage.free

    print(f"Total space:    {total_space    / ( 1024 ** 3 ):.2f} GB")
    print(f"Used space:     {used_space     / ( 1024 ** 3 ):.2f} GB")
    print(f"Free space:     {free_space     / ( 1024 ** 3 ):.2f} GB")

    return [total_space, used_space, free_space]

# returns the size of a folder path in bytes
def get_folder_size(folder_path):
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
            # print(total_size)

    size_bytes = total_size

    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    size_gb = size_mb / 1024

    # print(f"Total size: {size_bytes} bytes, {size_kb:.2f} KB, {size_mb:.2f} MB, {size_gb:.2f} GB")

    return total_size

# spaceReport = get_disk_space("c:/")
# print(spaceReport)

# curSize = get_folder_size(R"U:\Assets")
# print(curSize)