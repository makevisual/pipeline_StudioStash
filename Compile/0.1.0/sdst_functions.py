import psutil #psutil is a secondary package
import os
import datetime
from tkinter import filedialog

# cleans up the filepath
def clean_file_path(input_path):
    # Replace single slashes with double slashes
    cleaned_path = input_path.replace('\\', '\\\\')
    return cleaned_path

# returns the size of a disk, returning a list with the total_space, used_space, and free_space, in bytes
def get_disk_space(path):
    disk_usage = psutil.disk_usage(path)
    total_space = disk_usage.total
    used_space = disk_usage.used
    free_space = disk_usage.free

    # print(f"Total space:    {total_space    / ( 1024 ** 3 ):.2f} GB")
    # print(f"Used space:     {used_space     / ( 1024 ** 3 ):.2f} GB")
    # print(f"Free space:     {free_space     / ( 1024 ** 3 ):.2f} GB")

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

# Update the sizes on each of the copyOperations
def weighCopyOps(sdstData):
    for op in sdstData.copyOperations:
        print("Calculating size: ", op.pathSrc )
        op.pathSrcSize = get_folder_size(op.pathSrc)

# saves the passed content string out as a .bat file for processing later
def bat_saveAs(contentStr):

    current_datetime = datetime.datetime.now()
    current_datetime_str = current_datetime.strftime("%Y_%m_%d__%H-%M-%S")

    default_file_name = ("StudioStash__ArchiveOperations__" + current_datetime_str)

    file_path = filedialog.asksaveasfilename(defaultextension=".bat", initialfile=default_file_name, filetypes=[("Batch processing file", "*.bat")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(contentStr)