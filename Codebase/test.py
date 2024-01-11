import subprocess
import os

folder_path = r"C:\path\to\your\folder"

# Check if the folder path exists
if os.path.exists(folder_path):
    # Use the 'start' command to open the folder in Windows
    subprocess.Popen(['start', 'explorer', folder_path], shell=True)
else:
    print(f"The folder '{folder_path}' does not exist.")
