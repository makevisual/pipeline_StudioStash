from tkinter import filedialog
from tkinter import Tk

# Create a Tkinter root window (it will not be shown)
root = Tk()
root.withdraw()  # Hide the main window

# Ask the user to select a directory
selected_directory = filedialog.askdirectory(title="Select Directory")

# Print the selected directory (you can use it to save your file)
print("Selected Directory:", selected_directory)
